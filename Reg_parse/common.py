
#=====================================================================
#Define log print
#---------------------------------------------------------------------
import logging
#logging.basicConfig(level = logging.INFO,format = ("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
logging.basicConfig(level = logging.INFO,format = ("%(levelname)s: %(pathname)s[line:%(lineno)d] - %(message)s"))
logger = logging.getLogger(__name__)
 
#logger.info("Start print log")
#logger.debug("Do something")
#logger.warning("Something maybe fail.")
#logger.info("Finish")

# FATAL,CRITICAL,ERROR,WARNING,ONFO,DEBUG
logger.setLevel(logging.INFO)  # 重新设定Log等级开关
#=====================================================================


def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e: #转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)

def strQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])
