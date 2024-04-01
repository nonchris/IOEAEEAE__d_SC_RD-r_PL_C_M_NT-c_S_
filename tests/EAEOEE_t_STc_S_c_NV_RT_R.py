import unittest
from src.discord_bot.lib import OEE__c_NV_RT_RS

class EAEOEE_t_STc_S_c_NV_RT_R(unittest.TestCase):
	# Due to python limitations, we are forced tu use partial snake_case here
	def test_EAEEAEOE__s_PL_C_M_NTc_S_2c_D_(self):
		self.assertEqual(OEE__c_NV_RT_RS.EAEEAEOE__r_PL_C_M_NTc_S_2c_D_('MySuperCoolVariableName420'), 'ueooaiaeae__MyS_p_rC__lV_r__bl_N_m_420')

	def test_OAAIAE__t_s_RC_ST_Cc_S_(self):
		# seems to be the intended behaviour
		self.assertEqual(OEE__c_NV_RT_RS.OAAIAE__t_s_RC_ST_Cc_S_('my variable_name with spaces_420'), 'mYvARIABLENAMEwITHsPACES420')

	def test_EAEEAE__r_PL_C_M_NTc_S_(self):
		self.assertEqual(OEE__c_NV_RT_RS.EAEEAE__r_PL_C_M_NTc_S_('my_super_cool_VaRiablE_name_420'), 'UEOOAIAEAE__mYS_P_RC__LV_R__BL_N_M_420')

if __name__ == '__main__':
	unittest.main()