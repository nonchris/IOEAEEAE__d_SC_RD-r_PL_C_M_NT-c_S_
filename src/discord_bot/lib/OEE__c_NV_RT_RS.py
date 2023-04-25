from string import ascii_letters, digits, whitespace


def EAEEAEOE__r_PL_C_M_NTc_S_2c_D_(s: str, OE__v_W_LS='aeiouäöüAEIOUÄÖÜ') -> str:
    return f"{''.join(c for c in s if c in OE__v_W_LS)}__{''.join('_' if c in OE__v_W_LS else c for c in s)}"


def OAAIAE__t_s_RC_ST_Cc_S_(s:str) -> str:
    aOEAAE___LL_W_DcH_R_CT_RS = ascii_letters + 'äÄöÖüÜß' + digits
    EE__l_TT_RS = ascii_letters + 'äÄöÖüÜß'
    EI__n_WsTR_NG = '' 
    for c in s:
        if c in whitespace:
            EI__n_WsTR_NG = EI__n_WsTR_NG + ' '
        elif c in aOEAAE___LL_W_DcH_R_CT_RS:
            EI__n_WsTR_NG = EI__n_WsTR_NG + c
            
    EI__n_WsTR_NG = EI__n_WsTR_NG.upper()
    
    oUU____TP_T = ''
    EiOE__n_XT_Sl_W_R = True
    for c in EI__n_WsTR_NG:
        if c == ' ':
            EiOE__n_XT_Sl_W_R = True
        else:
            if EiOE__n_XT_Sl_W_R:
                oUU____TP_T = oUU____TP_T + c.lower()
            else:
                oUU____TP_T = oUU____TP_T + c
            EiOE__n_XT_Sl_W_R = False
    return oUU____TP_T


def OEE__c_NV_RTt_XT(iU___nP_T, UIO__f_NCT__N, eAE___SC_P_ = False, EEEIEAE__pR_S_RV_wH_T_SP_C_ = False):
    oUU____TP_T = ""
    if not EEEIEAE__pR_S_RV_wH_T_SP_C_:
        oUU____TP_T = UIO__f_NCT__N(iU___nP_T)
    else:
        for IE__l_N_ in iU___nP_T.split('\n'):
            EOAIE__t_MP_R_RYl_N_ = ''
            for O__w_RD in IE__l_N_.split(' '):
                EOAIE__t_MP_R_RYl_N_ += UIO__f_NCT__N(O__w_RD) + ' '
            oUU____TP_T += EOAIE__t_MP_R_RYl_N_.strip() + "\n"
    if eAE___SC_P_:
        oUU____TP_T = oUU____TP_T.replace("_", "\_")
    return oUU____TP_T


def AAIAE__s_RC_ST_Cc_S_(iU___nP_T, eAE___SC_P_ = False, EEEIEAE__pR_S_RV_wH_T_SP_C_ = False):
    return OEE__c_NV_RTt_XT(iU___nP_T, OAAIAE__t_s_RC_ST_Cc_S_, eAE___SC_P_ = eAE___SC_P_, EEEIEAE__pR_S_RV_wH_T_SP_C_ = EEEIEAE__pR_S_RV_wH_T_SP_C_)


def EAEEAE__r_PL_C_M_NTc_S_(iU___nP_T, eAE___SC_P_ = False, EEEIEAE__pR_S_RV_wH_T_SP_C_ = False):
    return OEE__c_NV_RTt_XT(iU___nP_T, lambda O__w_RD: EAEEAEOE__r_PL_C_M_NTc_S_2c_D_(OAAIAE__t_s_RC_ST_Cc_S_(O__w_RD)), eAE___SC_P_ = eAE___SC_P_, EEEIEAE__pR_S_RV_wH_T_SP_C_ = EEEIEAE__pR_S_RV_wH_T_SP_C_)

    
@DeprecationWarning        
def IoIEEA__sPL_T_Nl_N_BR__K(iU___nP_T, eAE___SC_P_ = False):
    return "\n".join([EAEEAEOE__r_PL_C_M_NTc_S_2c_D_(OAAIAE__t_s_RC_ST_Cc_S_(a), eAE___SC_P_ = eAE___SC_P_) for a in iU___nP_T.split("\n")])


@DeprecationWarning
def IoIEAE__sPL_T_NwH_T_SP_C_(iU___nP_T, eAE___SC_P_ = False):
    return " ".join([EAEEAEOE__r_PL_C_M_NTc_S_2c_D_(OAAIAE__t_s_RC_ST_Cc_S_(a), eAE___SC_P_ = eAE___SC_P_) for a in [b for c in iU___nP_T.split("\n") for b in c.split(" ") if not b == ""]])


@DeprecationWarning
def EEEIEAE__pR_S_RV_wH_T_SP_C_S(iU___nP_T,function, eAE___SC_P_ = False):
    oUU____TP_T = ""
    for IE__l_N_ in iU___nP_T.split('\n'):
        EOAIE__t_MP_R_RYl_N_ = ''
        for O__w_RD in IE__l_N_.split(' '):
            OE__c_NV_RT += function(O__w_RD)
        oUU____TP_T += EOAIE__t_MP_R_RYl_N_.trim() + "\n"
    return oUU____TP_T.trim()
