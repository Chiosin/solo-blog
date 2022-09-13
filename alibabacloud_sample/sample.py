# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List
from Tea.core import TeaCore

from alibabacloud_waf_openapi20190910.client import Client as waf_openapi20190910Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_waf_openapi20190910 import models as waf_openapi_20190910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> waf_openapi20190910Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'wafopenapi.cn-hangzhou.aliyuncs.com'
        return waf_openapi20190910Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('xxx', 'xxxx')
        create_protection_module_rule_request = waf_openapi_20190910_models.CreateProtectionModuleRuleRequest(
            instance_id='waf-cn-4591mheit02',
            defense_type='ac_custom',
            domain='www.lfzj.edu.cn',
            rule='{"action":"monitor","name":"test111","scene":"custom_acl","conditions":[{"opCode":1,"key":"IP","values":"10.8.8.8"}]}'
        )
        runtime = util_models.RuntimeOptions()
        resp = client.create_protection_module_rule_with_options(create_protection_module_rule_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        create_protection_module_rule_request = waf_openapi_20190910_models.CreateProtectionModuleRuleRequest(
            instance_id='waf-cn-4591mheit02',
            defense_type='ac_custom',
            domain='www.lfzj.edu.cn',
            rule='{"action":"monitor","name":"security_soar_ip_8.8.8.8","scene":"custom_acl","conditions":[{"opCode":51,"key":"IP","values":"8.8.8.8"}]}'
        )
        runtime = util_models.RuntimeOptions()
        resp = await client.create_protection_module_rule_with_options_async(create_protection_module_rule_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
