# 每款保险的url和断言
LANDING_PAGES_LINKS = {
    "passportLogin":"https://passport.qschou.com/sdk/v5/login.html?passport_scene=jb_qsb_yesph_2&redirect_url=https%3A%2F%2Fm.qsebao.com%2Fzbb%2Fpersonal%2Fcenter",

    #泰康30重疾直赔
    "taikang_illness":{
        "url":"https://m.qsebao.com/zbb/landpage?sku_name=taikang-illness&scene_name=taikang-illness-land-page",
        "privacy_policy_expect":"即表示您已充分理解并同意本政策",
        "rate_table_expect":"30天~1岁(不含)",
        "health_notification_expect":"未曾有体检医师或医生给被保险人提出复查",
        "insurance_clause_expect":"C00019932612020081001581",
        "insurance_notice_expect":"电子保单与纸质保单具有同等法律效力",
        "registration_agreement_expect":"平台相关服务所订立的协议",
        "customer_notification_expect":"我公司应履行客户告知义务"

    },
    #泰康全民癌症
    "taikang-health-quanmin-aizheng":{
        "url":"https://m.qsebao.com/zbb/landpage?scene_name=taikang-health-quanmin-aizheng-land-page-kuaishou-month&sku_name=taikang-health-quanmin-aizheng",
        "insurance_notice_expect": "本产品由泰康在线财产保险股份有限公司承保",
        "insurance_clause_expect": "本保险合同（以下简称“本合同”)由保险条款",
        "health_notification_expect": "1、被保险人未被诊断患有以下任一疾病，或未出现以下任一体征或检查异常：",
        "rate_table_expect": "2-12月(月付)",
        "special_agreement_expect":"本保单对被保险人在上海市质子重离子医院接受质子重离子治疗所支付的医疗费",
        "important_tips_expect":"1、等待期：本产品针对首次投保或非续保的保单，自保险合同生效之日起等待期为90天。 ",
        "registration_agreement_expect": "本协议是广东轻松保保险经纪有限公司",
        "customer_notification_expect": "感谢您委托广东轻松保保险经纪有限公司",
        "privacy_policy_expect": "您需在充分理解并同意本政策"
    }

}
