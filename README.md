# Welcome to your CDK Python project!

Jsii subclass repro:

```
cdk synth
```

Leads to

```
Traceback (most recent call last):
  File "/Users/huijbers/Temp/pythonpipesrepro/app.py", line 47, in <module>
    app.synth()
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/aws_cdk/core/__init__.py", line 16432, in synth
    return typing.cast(aws_cdk.cx_api.CloudAssembly, jsii.invoke(self, "synth", [options]))
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/jsii/_kernel/__init__.py", line 128, in wrapped
    return _recursize_dereference(kernel, fn(kernel, *args, **kwargs))
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/jsii/_kernel/__init__.py", line 348, in invoke
    return _callback_till_result(self, response, InvokeResponse)
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/jsii/_kernel/__init__.py", line 216, in _callback_till_result
    response = kernel.sync_complete(
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/jsii/_kernel/__init__.py", line 386, in sync_complete
    return self.provider.sync_complete(
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/jsii/_kernel/providers/process.py", line 382, in sync_complete
    resp = self._process.send(_CompleteRequest(complete=request), response_type)
  File "/Users/huijbers/Temp/pythonpipesrepro/.venv/lib/python3.9/site-packages/jsii/_kernel/providers/process.py", line 326, in send
    raise JSIIError(resp.error) from JavaScriptError(resp.stack)
jsii.errors.JSIIError: '' object has no attribute 'add_action'
```


Leading up to trace:

```
> {
  "fqn": "@aws-cdk/pipelines.Step",
  "args": [
    "some"
  ],
  "overrides": [
    {
      "method": "produceAction",
      "property": null,
      "cookie": "produce_action"
    }
  ],
  "interfaces": [
    "@aws-cdk/pipelines.IFileSetProducer"
  ],
  "api": "create"
}

< {"callback":{"cookie":"produce_action","cbid":"jsii::callback::20000","invoke":{"objref":{"$jsii.byref":"@aws-cdk/pipelines.Step@10008"},"method":"produceAction","args":[{"$jsii.byref":"Object@10010"},{"actionName":"some","runOrder":1,"artifacts":{"$jsii.byref":"@aws-cdk/pipelines.ArtifactMap@10011"},"scope":{"$jsii.byref":"@aws-cdk/core.Construct@10012"},"fallbackArtifact":{"$jsii.byref":"@aws-cdk/aws-codepipeline.Artifact@10013"},"pipeline":{"$jsii.byref":"@aws-cdk/pipelines.CodePipeline@10006"},"codeBuildDefaults":{"buildEnvironment":{"buildImage":{"$jsii.byref":"@aws-cdk/aws-codebuild.LinuxBuildImage@10014"},"computeType":"BUILD_GENERAL1_SMALL"}},"beforeSelfMutation":false}]}}}
> {"complete":{"cbid":"jsii::callback::20000","err":"'' object has no attribute 'add_action'","result":null,"api":"complete"}}
```

Looks like the `IStage` that's getting passed into the callback doesn't have the `add_action` method, probably because
the interfaces aren't discovered properly.
