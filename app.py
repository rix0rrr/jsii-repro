#!/usr/bin/env python3
from aws_cdk import core, pipelines, aws_codepipeline_actions, aws_codepipeline, aws_stepfunctions
import jsii


@jsii.implements(pipelines.ICodePipelineActionFactory)
class SomeStep(pipelines.Step):
    def __init__(self, id_):
        super().__init__(id_)

    @jsii.member(jsii_name="produceAction")
    def produce_action(
            self, stage: aws_codepipeline.IStage,
            options: pipelines.ProduceActionOptions,
            # TODO why are these not passed?
            # *,
            # action_name, artifacts, pipeline, run_order, scope,
            # before_self_mutation=None,
            # code_build_defaults=None,
            # fallback_artifact=None
    ) -> pipelines.CodePipelineActionFactoryResult:
        stage.add_action(
            aws_codepipeline_actions.StepFunctionInvokeAction(
                state_machine=aws_stepfunctions.StateMachine.from_state_machine_arn("..."),
                action_name="foo",
                state_machine_input=aws_codepipeline_actions.StateMachineInput.literal({"foo": "bar"}),
                run_order=options["run_order"],
            )
        )

        return pipelines.CodePipelineActionFactoryResult(run_orders_consumed=1)


app = core.App()

stage = core.Stage(app, "stage")
stack = core.Stack(stage, "stack")
pipeline_stack = core.Stack(app, "pipeline-stack")
pipeline = pipelines.CodePipeline(
    pipeline_stack,
    "pipeline",
    synth=pipelines.ShellStep("synth", input=pipelines.CodePipelineSource.git_hub("foo/bar", "main"), commands=["cdk synth"])
)

pipeline.add_wave("wave").add_stage(stage, pre=[SomeStep("some")])

app.synth()