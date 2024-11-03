import os
from decorators import secret_parameter, env_parameter


class Config:
    stage = os.environ.get("STAGE", "dev")

    @secret_parameter(secret_name=f"rdr/{stage}/dcx_api/url")
    def DCX_API_URL(self):
        pass

    @secret_parameter(secret_name=f"rdr/{stage}/dcx_api/headers/source_system")
    def DCX_API_SOURCE_SYSTEM(self):
        pass

    @secret_parameter(secret_name=f"rdr/{stage}/dcx_api/s3_bucket_name")
    def DCX_S3_BUCKET_NAME(self):
        pass

    @secret_parameter(secret_name=f"rdr/{stage}/common_secrets", key="dcx_api_key")
    def DCX_API_API_KEY(self):
        pass

    @env_parameter(env_name="SOURCE_SYSTEM")
    def SOURCE_SYSTEM(self):
        pass
