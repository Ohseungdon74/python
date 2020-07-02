#-*- coding: euc-kr -*-

def errors(err_code):

    err_dic = {0:('OP_ERR_NONE', '����ó��'),
               -10:('OP_ERR_FAIL', '����'),
               -100:('OP_ERR_LOGIN', '�����������ȯ����'),
               -101:('OP_ERR_CONNECT', '�������ӽ���'),
               -102:('OP_ERR_VERSION', '����ó������'),
               -103:('OP_ERR_FIREWALL', '���ι�ȭ������'),
               -104:('OP_ERR_MEMORY', '�޸𸮺�ȣ����'),
               -105:('OP_ERR_INPUT', '�Լ��Է°�����'),
               -106:('OP_ERR_SOCKET_CLOSED', '��ſ�������'),
               -200:('OP_ERR_SISE_OVERFLOW', '�ü���ȸ������'),
               -201:('OP_ERR_RQ_STRUCT_FAIL', '�����ۼ��ʱ�ȭ����'),
               -202:('OP_ERR_RQ_STRING_FAIL', '�����ۼ��Է°�����'),
               -203:('OP_ERR_NO_DATA', '�����;���'),
               -204:('OP_ERR_OVER_MAX_DATA', '��ȸ������������ʰ�'),
               -205:('OP_ERR_DATA_RCV_FAIL', '�����ͼ��Ž���'),
               -206:('OP_ERR_OVER_MAX_FID', '��ȸ������FID���ʰ�'),
               -207:('OP_ERR_REAL_CANCEL', '�ǽð���������'),
               -300:('OP_ERR_ORD_WRONG_INPUT', '�Է°�����'),
               -301:('OP_ERR_ORD_WRONG_ACCTNO', '���º�й�ȣ����'),
               -302:('OP_ERR_OTHER_ACC_USE', 'Ÿ�ΰ��»�����'),
               -303:('OP_ERR_MIS_2BILL_EXC', '�ֹ�������20������ʰ�'),
               -304:('OP_ERR_MIS_5BILL_EXC', '�ֹ�������50������ʰ�'),
               -305:('OP_ERR_MIS_1PER_EXC', '�ֹ��������ѹ����ּ���1 % �ʰ�����'),
               -306:('OP_ERR_MIS_3PER_EXC', '�ֹ��������ѹ����ּ���3 % �ʰ�����'),
               -307:('OP_ERR_SEND_FAIL', '�ֹ����۽���'),
               -308:('OP_ERR_ORD_OVERFLOW', '�ֹ����۰�����'),
               -309:('OP_ERR_MIS_300CNT_EXC', '�ֹ�����300����ʰ�'),
               -310:('OP_ERR_MIS_500CNT_EXC', '�ֹ�����500����ʰ�'),
               -340:('OP_ERR_ORD_WRONG_ACCTINFO', '������������'),
               -500:('OP_ERR_ORD_SYMCODE_EMPTY', '�����ڵ����')
               }

    result = err_dic[err_code]

    return result