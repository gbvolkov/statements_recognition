from BankStatement_1_process import BankStatement_1_process
from BankStatement_2_process import BankStatement_2_process
from BankStatement_3_process import BankStatement_3_process
from BankStatement_4_process import BankStatement_4_process
from BankStatement_5_process import BankStatement_5_process
from BankStatement_6_process import BankStatement_6_process
from BankStatement_7_process import BankStatement_7_process
from BankStatement_8_process import BankStatement_8_process
from BankStatement_9_process import BankStatement_9_process
from BankStatement_10_process import BankStatement_10_process
from BankStatement_11_process import BankStatement_11_process
from BankStatement_12_process import BankStatement_12_process
from BankStatement_13_process import BankStatement_13_process
from BankStatement_14_process import BankStatement_14_process
from BankStatement_15_process import BankStatement_15_process
from BankStatement_16_process import BankStatement_16_process
from BankStatement_17_process import BankStatement_17_process
from BankStatement_18_process import BankStatement_18_process
from BankStatement_19_process import BankStatement_19_process
from BankStatement_20_process import BankStatement_20_process
from BankStatement_21_process import BankStatement_21_process
from BankStatement_22_process import BankStatement_22_process
from BankStatement_23_process import BankStatement_23_process
from BankStatement_24_process import BankStatement_24_process
from BankStatement_25_process import BankStatement_25_process
from BankStatement_26_process import BankStatement_26_process
from BankStatement_27_process import BankStatement_27_process
from BankStatement_28_process import BankStatement_28_process
from BankStatement_29_process import BankStatement_29_process
from BankStatement_30_process import BankStatement_30_process
from BankStatement_31_process import BankStatement_31_process
from BankStatement_32_process import BankStatement_32_process
from BankStatement_33_process import BankStatement_33_process
from BankStatement_34_process import BankStatement_34_process
from BankStatement_35_process import BankStatement_35_process
from BankStatement_36_process import BankStatement_36_process
from BankStatement_37_process import BankStatement_37_process
from BankStatement_38_process import BankStatement_38_process
from BankStatement_39_process import BankStatement_39_process
from BankStatement_40_process import BankStatement_40_process
from BankStatement_41_process import BankStatement_41_process
from BankStatement_42_process import BankStatement_42_process
from BankStatement_43_process import BankStatement_43_process
from BankStatement_44_process import BankStatement_44_process
from BankStatement_45_process import BankStatement_45_process
from BankStatement_46_process import BankStatement_46_process
from BankStatement_47_process import BankStatement_47_process
from BankStatement_48_process import BankStatement_48_process
from BankStatement_49_process import BankStatement_49_process
from BankStatement_50_process import BankStatement_50_process
from BankStatement_51_process import BankStatement_51_process
from BankStatement_52_process import BankStatement_52_process
from BankStatement_53_process import BankStatement_53_process
from BankStatement_54_process import BankStatement_54_process
from BankStatement_55_process import BankStatement_55_process
from BankStatement_56_process import BankStatement_56_process
from BankStatement_57_process import BankStatement_57_process
from BankStatement_58_process import BankStatement_58_process
from BankStatement_59_process import BankStatement_59_process
from BankStatement_60_process import BankStatement_60_process
from BankStatement_NO_process import IgnoreHDR_process


HDRSIGNATURES = [{"датадокумента|датаоперации|n|бик|счет|контрагент|иннконтрагента|бикбанкаконтрагента|коррсчетбанкаконтрагента|наименованиебанкаконтрагента|счетконтрагента|списание|зачисление|назначениеплатежа|код": BankStatement_1_process},
                 {"датадокумента|датаоперации|n|бик|счет|контрагент|иннконтрагента|бикбанкаконтрагента|коррсчетбанкаконтрагента|наименованиебанкаконтрагента|счетконтрагента|списание|зачисление|назначениеплатежа|код|показательстатуса101|коддоходабюджетнойклассификации104|кодоктмо105|показательоснованияплатежа106|показательналоговогопериодакодтаможенногооргана107|показательномерадокумента108|показательдатыдокумента109|показательтипаплатежа110": BankStatement_1_process},
                 {"дата|видшифроперацииво|номердокументабанка|номердокумента|бикбанкакорреспондента|корреспондирующийсчет|суммаподебету|суммапокредиту": BankStatement_2_process},
                 {"датаоперации|номердокумента|дебет|кредит|контрагентнаименование|контрагентинн|контрагенткпп|контрагентбик|контрагентнаименованиебанка|назначениеплатежа|коддебитора|типдокумента": BankStatement_3_process},
                 {"датаоперации|номердокумента|дебет|кредит|контрагентнаименование|контрагентинн|контрагенткпп|контрагентсчет|контрагентбик|контрагентнаименованиебанка|назначениеплатежа|коддебитора|типдокумента": BankStatement_3_process},
                 {"nдок|датадокумента|датаоперации|реквизитыкорреспондентанаименование|реквизитыкорреспондентасчет|реквизитыкорреспондентаиннконтрагента|реквизитыкорреспондентабанк|дебетсуммасуммавнп|кредитсуммасуммавнп|курсцбнадатуоперации|основаниеоперацииназначениеплатежа": BankStatement_4_process},
                 {"дата|номердокумента|дебет|кредит|контрагентнаименование|контрагентинн|контрагенткпп|контрагентбик|контрагентнаименованиебанка|назначениеплатежа|типдокумента": BankStatement_5_process},
                 {"дата|номердокумента|дебет|кредит|контрагентнаименование|контрагентинн|контрагенткпп|контрагентбик|контрагентнаименованиебанка|назначениеплатежа|коддебитора|типдокумента": BankStatement_5_process},
                 {"дата|номердокумента|дебет|кредит|контрагентнаименование|контрагентинн|контрагенткпп|контрагентсчет|контрагентбик|контрагентнаименованиебанка|назначениеплатежа|коддебитора|типдокумента": BankStatement_5_process},
                 {"номердокумента|датадокумента|датаоперации|счет|контрагент|иннконтрагента|бикбанкаконтрагента|коррсчетбанкаконтрагента|наименованиебанкаконтрагента|счетконтрагента|списание|зачисление|назначениеплатежа": BankStatement_6_process},
                 {"templatecode|repstatementsrurexcelxls": IgnoreHDR_process},
                 {"номер|контрагент|реквизитыконтрагента|назначениеплатежа|дебет|кредит": IgnoreHDR_process},
                 {"xdo_?accountnumber?|<?dataean?>|<?dataean?>": IgnoreHDR_process},
                 {"датапроводки|счетдебет|счеткредит|суммаподебету|суммапокредиту|nдокумента|во|банкбикинаименование|назначениеплатежа": BankStatement_7_process},
                 {"датаопер|ко|номердокум|датадокум|дебет|кредит|рублевоепокрытие|контрагентинн|контрагенткпп|контрагентнаименование|контрагентсчет|контрагентбик|контрагенткоррсчет|контрагентбанк|клиентинн|клиентнаименование|клиентсчет|клиенткпп|клиентбин|клиенткоррсчет|клиентбанк|код|назначениеплатежа|очерплатежа|бюджетныйплатежстатуссост|бюджетныйплатежкбк|бюджетныйплатежоктмо|бюджетныйплатежоснование|бюджетныйплатежналогпериод|бюджетныйплатежномердок|idопер": BankStatement_8_process},
                 {"датаопер|ко|номердокум|датадокум|дебет|кредит|рублевоепокрытие|контрагентинн|контрагенткпп|контрагентнаименование|контрагентсчет|контрагентбик|контрагенткоррсчет|контрагентбанк|клиентинн|клиентнаименование|клиентсчет|клиенткпп|клиентбин|клиенткоррсчет|клиентбанк|назначениеплатежа|очерплатежа|idопер": BankStatement_8_process},
                 {"датаопер|ко|номердокум|датадокум|дебет|кредит|рублевоепокрытие|контрагентинн|контрагенткпп|контрагентнаименование|контрагентсчет|контрагентбик|контрагенткоррсчет|контрагентбанк|клиентинн|клиентнаименование|клиентсчет|клиенткпп|клиентбик|клиенткоррсчет|клиентбанк|резполе|код|кодвыплат|назначениеплатежа|очерплатежа|видусловияоплаты|основаниедлясписания|бюджетныйплатежстатуссост|бюджетныйплатежкбк|бюджетныйплатежоктмо|бюджетныйплатежоснование|бюджетныйплатежналогпериод|бюджетныйплатежномердок|бюджетныйплатеждатадок|idопер": BankStatement_8_process},
                 {"датаопер|ко|номердокум|датадокум|дебет|кредит|рублевоепокрытие|контрагентинн|контрагенткпп|контрагентнаименование|контрагентсчет|контрагентбик|контрагенткоррсчет|контрагентбанк|клиентинн|клиентнаименование|клиентсчет|клиенткпп|клиентбик|клиенткоррсчет|клиентбанк|резполе|код|кодвыплат|назначениеплатежа|очерплатежа|видусловияоплаты|основаниедлясписания|бюджетныйплатежстатуссост|бюджетныйплатежкбк|бюджетныйплатежоктмо|бюджетныйплатежоснование|бюджетныйплатежналогпериод|бюджетныйплатежномердок|бюджетныйплатеждатадок|idопер|idдокум": BankStatement_8_process},
                 {"датаопер|ко|номердокум|датадокум|дебет|кредит|рублевоепокрытие|контрагентинн|контрагенткпп|контрагентнаименование|контрагентсчет|контрагентбик|контрагенткоррсчет|контрагентбанк|клиентинн|клиентнаименование|клиентсчет|клиенткпп|клиентбик|клиенткоррсчет|клиентбанк|резполе|код|кодвыплат|назначениеплатежа|очерплатежа|видусловияоплаты|бюджетныйплатежстатуссост|бюджетныйплатежкбк|бюджетныйплатежоктмо|бюджетныйплатежоснование|бюджетныйплатежналогпериод|бюджетныйплатежномердок|бюджетныйплатеждатадок|idопер|idдокум": BankStatement_8_process},
                 {"датаопер|ко|номердокум|датадокум|дебет|кредит|рублевоепокрытие|контрагентинн|контрагенткпп|контрагентнаименование|контрагентсчет|контрагентбик|контрагенткоррсчет|контрагентбанк|клиентинн|клиентнаименование|клиентсчет|клиенткпп|клиентбик|клиенткоррсчет|клиентбанк|резполе|код|кодвыплат|назначениеплатежа|очерплатежа|видусловияоплаты|основаниедлясписания|бюджетныйплатежстатуссост|бюджетныйплатежкбк|бюджетныйплатежоктмо|бюджетныйплатежоснование|бюджетныйплатежналогпериод|бюджетныйплатежномердок|бюджетныйплатеждатадок|idопер|idдокум|кодвидадохода": BankStatement_8_process},
                 {"датаоперации|nдок|видоперации|контрагент|иннконтрагента|бикбанкаконтрагента|лицевойсчет|дебет|кредит|назначение": BankStatement_9_process},
                 {"датаоперации|nдок|видоперации|контрагент|иннконтрагента|бикбанкаконтрагента|лицевойсчет|дебет|кредит|назначение|суммавнацпокрытии|курс": BankStatement_9_process},
                 {"дата|видопер|nдок|бик|банкконтрагента|контрагент|иннконтрагента|счетконтрагента|дебетrub|кредитrub|операция": BankStatement_10_process},
                 {"дата|номер|видоперации|контрагент|иннконтрагента|бикбанкаконтрагента|счетконтрагента|дебетrur|кредитrur|назначение": BankStatement_11_process},
                 {"дата|ро|док|кб|внешсчет|счет|дебет|кредит|назначение|контрагент|контринн": BankStatement_12_process},
                 {"документ|датаоперации|корреспондентнаименование|корреспондентинн|корреспонденткпп|корреспондентсчет|корреспондентбик|вхостаток|оборотдт|обороткт|назначениеплатежа": BankStatement_13_process},
                 {"тип|дата|номер|видоперации|сумма|валюта|основаниеплатежа|бикбанкаполучателя|счетполучателя|наименованиеполучателя": BankStatement_14_process},
                 {"nпп|датаоперацииpostingdate|датавалютирvalue|видоперoptype|номердокументаdocumentnumber|реквизитыкорреспондентаcounterpartydetailsнаименованиеname|реквизитыкорреспондентаcounterpartydetailsсчетaccount|реквизитыкорреспондентаcounterpartydetailsбанкbank|дебетdebit|кредитcredit|основаниеоперацииназначениеплатежаpaymentdetails": BankStatement_15_process},
                 {"nпп|датаоперацииpostingdate|датавалютирvaluedate|видоперoptype|номердокументаdocumentnumber|реквизитыкорреспондентаcounterpartydetailsнаименованиеname|реквизитыкорреспондентаcounterpartydetailsсчетaccount|реквизитыкорреспондентаcounterpartydetailsбанкbank|дебетdebit|кредитcredit|основаниеоперацииназначениеплатежаpaymentdetails": BankStatement_15_process},
                 {"nдокумента|дата|бик|nсчета|дебоборот|кредоборот|иннинаименованиеполучателя|назначениеплатежа": BankStatement_16_process},
                 {"дата|nдок|во|банкконтрагента|контрагент|счетконтрагента|дебет|кредит|назначениеплатежа": BankStatement_17_process},
                 {"дата|no|во|бик|банкконтрагента|контрагент|иннконтрагента|счетконтрагента|дебет|кредит|назначениеплатежа": BankStatement_17_process},
                 {"nпп|датасовершенияоперацииддммгг|реквизитыдокументанаоснованиикоторогобыласовершенаоперацияпосчетуспециальномубанковскомусчетувидшифр|реквизитыдокументанаоснованиикоторогобыласовершенаоперацияпосчетуспециальномубанковскомусчетуномер|реквизитыдокументанаоснованиикоторогобыласовершенаоперацияпосчетуспециальномубанковскомусчетудата|реквизитыбанкаплательщикаполучателяденежныхсредствномеркорреспондентскогосчета|реквизитыбанкаплательщикаполучателяденежныхсредствнаименование|реквизитыбанкаплательщикаполучателяденежныхсредствбик|реквизитыплательщикаполучателяденежныхсредствнаименованиефио|реквизитыплательщикаполучателяденежныхсредствиннкио|реквизитыплательщикаполучателяденежныхсредствкпп|реквизитыплательщикаполучателяденежныхсредствномерсчетаспециальногобанковскогосчета|суммаоперациипосчетуспециальномубанковскомусчетуподебету|суммаоперациипосчетуспециальномубанковскомусчетупокредиту|назначениеплатежа": BankStatement_18_process},
                 {"номер|номерсчета|дата|контрагентcчет|контрагент|поступление|валюта|списание|валюта|назначение": BankStatement_19_process},
                 {"nпп|nдок|датаоперации|бикswiftбанкаплат|наименованиебанкаплательщика|наименованиеплательщика|иннплательщика|nсчетаплательщика|бикswiftбанкаполуч|наименованиебанкаполучателя|наименованиеполучателя|иннполучателя|nсчетаполучателя|сальдовходящее|дебет|кредит|сальдоисходящее|назначениеплатежа": BankStatement_20_process},
                 {"column|nпп|nдок|датаоперации|бикswiftбанкаплат|наименованиебанкаплательщика|наименованиеплательщика|иннплательщика|nсчетаплательщика|бикswiftбанкаполуч|наименованиебанкаполучателя|наименованиеполучателя|иннполучателя|nсчетаполучателя|сальдовходящее|дебет|кредит|сальдоисходящее|назначениеплатежа": BankStatement_20_process},
                 {"датадок|nдок|датаоперации|во|названиекорр|иннкорр|бикбанкакорр|счеткорр|дебет|кредит|назначение": BankStatement_21_process},
                 {"дата|nдок|во|названиекорр|иннконтрагента|бикбанкакорр|лицевойсчет|дебет|кредит|назначение": BankStatement_22_process},
                 {"дата|nдок|во|названиекорр|бикбанкакорр|лицевойсчет|дебет|кредит|назначение": BankStatement_22_process},
                 {"дата|nдок|во|бикбанкакорр|названиекорр|лицевойсчет|дебет|кредит|назначение": BankStatement_22_process},
                 {"номерстроки|датапроводки|видоперации|номердокумента|счетплательщикаполучателя|реквизитыплательщикаполучателяденежныхсредствнаименованиефио|реквизитыплательщикаполучателяденежныхсредствиннкио|реквизитыплательщикаполучателяденежныхсредствкпп|суммадебет|суммакредит|назначениеплатежа": BankStatement_23_process},
                 {"номерстроки|датапроводки|видоперации|датадокумента|номердокумента|счетплательщикаполучателя|реквизитыплательщикаполучателяденежныхсредствнаименованиефио|реквизитыплательщикаполучателяденежныхсредствиннкио|реквизитыплательщикаполучателяденежныхсредствкпп|суммадебет|суммакредит|назначениеплатежа": BankStatement_23_process},
                 {"номерстроки|датапроводки|видоперации|номердокумента|счетплательщикаполучателя|суммадебет|суммакредит|назначениеплатежа": BankStatement_23_process},
                 {"дата|n|клиентинн|клиентнаименование|клиентсчет|корреспондентбик|корреспондентсчет|корреспондентнаименование|во|содержание|оборотыдебет|оборотыкредит": BankStatement_24_process},
                 {"датаивремяпроводки|счеткорреспондента|дебет|кредит|исходящийостаток|наименованиекорреспондента|иннкорреспондента|назначениеплатежа": BankStatement_25_process},
                 {"датаоперации|номердокумента|дебет|кредит|контрагентнаименование|контрагентинн|контрагенткпп|контрагентбик|контрагентнаименованиебанка|назначениеплатежа|коддебитора|типдокумента": BankStatement_26_process},
                 {"номерстроки|датапроводки|видоперации|номердокументаклиента|номердокументабанканомердокументавсмфр|счетплательщикаполучателя|суммадебет|суммакредит|назначениеплатежа": BankStatement_27_process},
                 {"номерстроки|датапроводки|видоперации|номердокументаклиента|номердокументабанканомердокументавсмфр|счетплательщикаполучателя|наименованиекорреспондирующегосчета|суммадебет|суммакредит|назначениеплатежа": BankStatement_27_process},
                 {"датаивремяпроводки|входостаток|дебет|кредит|исходящийостаток|док|наименованиекорреспондента|иннкорреспондента|назначениеплатежа": BankStatement_28_process},
                 {"nпп|датасовершенияоперацииддммгг|реквизитыдокументанаоснованиикоторогобыласовершенаоперацияпосчетуспециальномубанковскомусчетувидшифр|реквизитыдокументанаоснованиикоторогобыласовершенаоперацияпосчетуспециальномубанковскомусчетуномер|реквизитыдокументанаоснованиикоторогобыласовершенаоперацияпосчетуспециальномубанковскомусчетудата|реквизитыбанкаплательщикаполучателяденежныхсредствномеркорреспондентскогосчета|реквизитыбанкаплательщикаполучателяденежныхсредствнаименование|реквизитыбанкаплательщикаполучателяденежныхсредствбик|реквизитыплательщикаполучателяденежныхсредствнаименованиефио|реквизитыплательщикаполучателяденежныхсредствиннкио|реквизитыплательщикаполучателяденежныхсредствкпп|реквизитыплательщикаполучателяденежныхсредствномерсчета|суммаоперациипосчетуподебету|суммаоперациипосчетупокредиту|назначениеплатежа": BankStatement_29_process},
                 {"датапроводки|во|nдок|банккорр|корреспондент|счетконтрагента|дебет|кредит|назначениеплатежа": BankStatement_30_process},
                 {"документ|датаоперации|корреспондентнаименование|корреспондентинн|корреспондентсчет|корреспондентбик|вхостаток|оборотдт|обороткт|назначениеплатежа": BankStatement_31_process},
                 {"дата|nдок|во|бикбанкаконтрагента|банкконтрагента|иннконтрагента|контрагент|счетконтрагента|дебет|кредит|назначениеплатежа": BankStatement_32_process},
                 {"датадокумента|номердокумента|поступление|списание|счеторганизации|организация|иннорганизации|счетконтрагента|контрагент|иннконтрагента|назначениеплатежа|коддебитора|типдокумента": BankStatement_33_process},
                 {"датадокумента|номердокумента|счеторганизации|организация|иннорганизации|счетконтрагента|контрагент|иннконтрагента|назначениеплатежа|поступление|списание|остатоквходящий|остатокисходящий|коддебитора|типдокумента": BankStatement_33_process},
                 {"датадокта|номердокта|корреспондентбанк|корреспондентсчет|корреспондентнаименование|видопер|оборотыподебету|оборотыпокредиту|назначениеплатежа": BankStatement_34_process},
                 {"датапроводки|nдокумента|клиентинн|клиентнаименование|клиентсчет|корреспондентбик|корреспондентбанк|корреспондентсчет|корреспондентинн|корреспондентнаименование|во|назначениеплатежа|оборотыдебет|оборотыкредит|референспроводки": BankStatement_35_process},
                 {"датапроводки|nдокумента|клиентинн|клиентнаименование|клиентсчет|корреспондентбик|корреспондентбанк|корреспондентсчет|корреспондентнаименование|во|назначениеплатежа|оборотыдебет|оборотыкредит|референспроводки": BankStatement_35_process},
                 {"номерсчета|идентификатортранзакции|типоперациипополнениесписание|категорияоперации|статус|датасозданияоперации|датаавторизации|дататранзакции|идентификатороригинальнойоперации|суммаоперацииввалютеоперации|валютаоперации|суммаввалютесчета|контрагент|иннконтрагента|кппконтрагента|счетконтрагента|бикбанкаконтрагента|коррсчетбанкаконтрагента|наименованиебанкаконтрагента|назначениеплатежа|номерплатежа|очередность|кодуин|номеркарты|mcc|местосовершениягород|местосовершениястрана|адресорганизации|банк|статуссоставителярасчетногодокумента|кбккодбюджетнойклассификации|кодоктмо|основаниеналоговогоплатежа|налоговыйпериодкодтаможенногооргана|номерналоговогодокумента|датаналоговогодокумента|типналоговогоплатежа": BankStatement_36_process},
                 {"номердокумента|ко|датаоперации|дебет|кредит|реквизитыконтрагентабик|реквизитыконтрагентанаименование|основаниеоперации": BankStatement_37_process},
                 {"nпп|датадокументаdocumentdate|датавалютирvaluedate|видоперoptype|реквизитыкорреспондентаcounterpartydetailsбикbic|реквизитыкорреспондентаcounterpartydetailsсчетaccount|реквизитыкорреспондентаcounterpartydetailsиннinn|реквизитыкорреспондентаcounterpartydetailsкппkpp|реквизитыкорреспондентаcounterpartydetailsнаименованиеname|дебетdebit|кредитcredit|основаниеоперацииназначениеплатежаpaymentdetails": BankStatement_38_process},
                 {"датаоперации|номердокумента|суммаподебету|суммапокредиту|контрагентсчетинннаименование|контрагентбанкбикнаименование|назначениеплатежа|коддебитора|типдокумента": BankStatement_39_process},
                 {"nдок|датадокумента|датаоперации|реквизитыкорреспондентанаименование|реквизитыкорреспондентасчет|реквизитыкорреспондентаиннконтрагента|реквизитыкорреспондентабанк|дебетсуммасуммавнп|кредитсуммасуммавнп|курсцбнадатуоперации|основаниеоперацииназначениеплатежа": BankStatement_40_process},
                 {"nn|датапров|во|номдок|бик|счеткорреспондент|дебет|кредит|основание|основание": BankStatement_41_process},
                 {"n|дата|счеткорреспондент|оборотдебет|обороткредит|примечание": BankStatement_42_process},
                 {"дата|номер|дебет|кредит|контрагентнаименованиеиннкппсчет|контрагентбанкбикнаименование|назначениеплатежа|коддебитор|документ": BankStatement_43_process},
                 {"дата|номер|дебет|кредит|контрагентнаименованиеиннкппсчет|контрагентбанкбикнаименование|назначениеплатежа|коддебитора|документ": BankStatement_43_process},
                 {"номердокумента|ко|датаоперации|дебет|кредит|реквизитыкорреспондентабик|реквизитыкорреспондентанаименование|основаниеоперации": BankStatement_44_process},
                 {"column|no|контрагент|иннконтрагента|счетконтрагента|дебет|кредит|назначениеплатежа": BankStatement_45_process},
                 {"no|датаоперации|nдокумента|шифрдокумента|бикбанкакорреспондента|наименованиекорреспондента|nсчетакорреспондента|дебет|кредит|суммавнацпокрытии|назначениеплатежа": BankStatement_46_process},
                 {"дата|nдок|во|названиекорр|иннкорр|бикбанкакорр|счеткорр|дебет|кредит|назначение": BankStatement_47_process},
                 {"датаоперации|датадокумента|во|nдокта|коррсчет|бик|наименованиебанка|счет|иннинаименованиекорреспондента|дебет|кредит|назначениеплатежа": BankStatement_48_process},
                 {"номерстроки|датапроводки|видоперации|номердокументаклиента|номердокументабанканомердокументавсмфр|счетплательщикаполучателя|дебет|кредит|остаток|назначениеплатежа": BankStatement_49_process},
                 {"датаоперации|номердокумента|корреспондентнаименованиеинн|корреспондентномерсчета|корреспондентнаименованиебанкабик|дебет|кредит|назначениеплатежа": BankStatement_50_process},
                 {"дата|n|во|контрагентинн|контрагентбикбанка|контрагентсчет|контрагентнаименование|оборотыrurдебет|оборотыrurкредит|назначение": BankStatement_51_process},
                 {"датапроводки|счетдебет|счеткредит|сумма|nдок|вид|во|банккоррбикинаименование|назначениеплатежа": BankStatement_52_process},
                 {"дата|n|иннплательщика|иннполучателя|корреспондентбик|корреспондентсчет|корреспондентнаименование|во|содержание|оборотыrurдебет|оборотыrurкредит": BankStatement_53_process},
                 {"документ|датаоперации|корреспондент|оборотдт|обороткт|назначениеплатежа": BankStatement_54_process},
                 {"датапроводки|во|номдок|банккорр|названиекорреспондента|счетплательщика|счетполучателя|дебет|кредит|назначениеплатежа": BankStatement_55_process},
                 {"датаучетаbalancedate|реквизитыдокументавидnдатаdocument:typendate|корреспондентcorrespondent|содержаниеоперацииtransactiondescription|оборотыamountдебетdebet|оборотыamountкредитcredit": BankStatement_56_process},
                 {"датадок|во|nдокум|бикбанкаконтраг|корреспондирующийсчет|оборотподебету|оборотпокредиту|инннаименованиеконтрагента|счетконтрагента|назначениеплатежа": BankStatement_57_process},
                 {"датадок|no|контрагент|счетконтрагента|дебет|кредит|назначениеплатежа": BankStatement_58_process},
                 {"nпп|датадокументаdocumentdate|датавалютирvaluedate|видоперoptype|реквизитыкорреспондентаcounterpartydetailsнаименованиеname|реквизитыкорреспондентаcounterpartydetailsиннinn|реквизитыкорреспондентаcounterpartydetailsкппkpp|реквизитыкорреспондентаcounterpartydetailsсчетaccount|реквизитыкорреспондентаcounterpartydetailsбикbik|реквизитыкорреспондентаcounterpartydetailsбанкbank|списаноdebit|зачисленоcredit|основаниеоперацииназначениеплатежаpaymentdetails": BankStatement_59_process},
                 {"датаоперации|номертипдокумента|корреспондентнаименованиеинн|корреспондентномерсчета|корреспондентнаименованиебанкабик|дебет|кредит|назначениеплатежа": BankStatement_60_process},
                 ]