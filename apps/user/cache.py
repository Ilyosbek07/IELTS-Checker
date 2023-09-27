class CacheTypes:
    registration_sms_verification = "registration_sms_verification"
    forget_pass_verification = "forget_pass_verification"


def generate_cache_key(type_, *args):
    return f"{type_}{''.join(args)}"
