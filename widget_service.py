from aws_cdk import(
    core as cdk,
    aws_apigateway as apigateway,
    aws_lambda as afunc,
    aws_s3 as as3
)

class WidgetService(cdk.Stack):
    def __init__(self, scope:cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        bucket = as3.Bucket(self, "WidgetStore")

        handler = afunc.Function(
            self, 
            "WidgetHandler",
            runtime= afunc.Runtime.NODEJS_10_X,
            code= afunc.Code.asset("resources"),
            handler= "widgets.main",
            environment= {"BUCKET": bucket.bucket_name}
        )

        api = apigateway.RestApi(
            self, 
            "widgets_api",
            rest_api_name="Widget Service",
            description= "This service serves widgets."
        )

        getWidgetsIntegration = apigateway.LambdaIntegration(
            handler,
            request_templates= {"application/json":'{"status":"200"}'}
        )

        api.root.add_method("GET", getWidgetsIntegration)
