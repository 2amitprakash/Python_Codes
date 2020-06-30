from openpyxl import Workbook
from openpyxl import load_workbook
import datetime
import common.connect_soch as conn
import pandas as pd

def fetch_data():
    sql = 'Select \
            table3."Received_Month",	\
            table3."Received_Year",\
            SUM(table3."Number_of_individuals_received_pre-test_counseling/information")"Number_of_individuals_received_pre-test_counseling/information",\
            SUM(table3."Number_of_individuals_receiving_post-test_counseling_and_given_results")"Number_of_individuals_receiving_post-test_counseling_and_given_results",\
            SUM(table3."Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling")"Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling",\
            SUM(table3."Number_of_individuals_tested_for_HIV")"Number_of_individuals_tested_for_HIV",\
            SUM(table3."Number_of_individuals_received_result_within_7_days_of_HIV_Test")"Number_of_individuals_received_result_within_7_days_of_HIV_Test",\
            SUM(table3."Number_of_HIV_positive_individuals_having_HIV-I_infection")"Number_of_HIV_positive_individuals_having_HIV-I_infection",\
            SUM(table3."Number_of_HIV_positive_individuals_having_HIV-II_infection")"Number_of_HIV_positive_individuals_having_HIV-II_infection",\
            SUM(table3."Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections")"Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections",\
            SUM(table3."Number_of_individuals_tested_for_HIV_and_found_Negative")"Number_of_individuals_tested_for_HIV_and_found_Negative",\
            SUM(table3."Number_of_Self-initiated_Individuals_tested_for_HIV")"Number_of_Self-initiated_Individuals_tested_for_HIV",\
            SUM(table3."Number_of_Self-initiated_individuals_diagnosed_HIV_positive")"Number_of_Self-initiated_individuals_diagnosed_HIV_positive",\
            SUM(table3."Number_of_provider_initiated_Individuals_tested_for_HIV")"Number_of_provider_initiated_Individuals_tested_for_HIV",\
            SUM(table3."Number_of_provider_initiated_individuals_diagnosed_HIV_positive")"Number_of_provider_initiated_individuals_diagnosed_HIV_positive",\
            SUM(table3."Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC")"Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC" \
            from( \
            select \
            table2."SACS_ID" ,\
            table2."SACS",\
            table2."Received_Month",\
            table2."Received_Year",\
            SUM(table2."Number_of_individuals_received_pre-test_counseling/information")"Number_of_individuals_received_pre-test_counseling/information",\
            SUM(table2."Number_of_individuals_receiving_post-test_counseling_and_given_results")"Number_of_individuals_receiving_post-test_counseling_and_given_results",\
            SUM(table2."Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling")"Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling",\
            SUM(table2."Number_of_individuals_tested_for_HIV")"Number_of_individuals_tested_for_HIV",\
            SUM(table2."Number_of_individuals_received_result_within_7_days_of_HIV_Test")"Number_of_individuals_received_result_within_7_days_of_HIV_Test",\
            SUM(table2."Number_of_HIV_positive_individuals_having_HIV-I_infection")"Number_of_HIV_positive_individuals_having_HIV-I_infection",\
            SUM(table2."Number_of_HIV_positive_individuals_having_HIV-II_infection")"Number_of_HIV_positive_individuals_having_HIV-II_infection",\
            SUM(table2."Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections")"Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections",\
            SUM(table2."Number_of_individuals_tested_for_HIV_and_found_Negative")"Number_of_individuals_tested_for_HIV_and_found_Negative",\
            SUM(table2."Number_of_Self-initiated_Individuals_tested_for_HIV")"Number_of_Self-initiated_Individuals_tested_for_HIV",\
            SUM(table2."Number_of_Self-initiated_individuals_diagnosed_HIV_positive")"Number_of_Self-initiated_individuals_diagnosed_HIV_positive",\
            SUM(table2."Number_of_provider_initiated_Individuals_tested_for_HIV")"Number_of_provider_initiated_Individuals_tested_for_HIV",\
            SUM(table2."Number_of_provider_initiated_individuals_diagnosed_HIV_positive")"Number_of_provider_initiated_individuals_diagnosed_HIV_positive",\
            SUM(table2."Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC")"Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC"\
            \
            from\
            (\
            Select \
            T2.ID,\
            T2."SACS",\
            T2."ICTC_center",\
            T2."SACS_ID", \
            CASE WHEN T2."Received_Month" = 1 THEN '"'January'"' \
                WHEN T2."Received_Month" = 2 THEN '"'February'"' \
                WHEN T2."Received_Month" = 3 THEN '"'March'"' \
                WHEN T2."Received_Month" = 4 THEN '"'April'"' \
                WHEN T2."Received_Month" = 5 THEN '"'May'"' \
                WHEN T2."Received_Month" = 6 THEN '"'June'"' \
                WHEN T2."Received_Month" = 7 THEN '"'July'"' \
                WHEN T2."Received_Month" = 8 THEN '"'August'"' \
                WHEN T2."Received_Month" = 9 THEN '"'September'"' \
                WHEN T2."Received_Month" = 10 THEN '"'October'"' \
                WHEN T2."Received_Month" = 11 THEN '"'November'"' \
                WHEN T2."Received_Month" = 12 THEN '"'December'"' \
            END as "Received_Month",\
            T2."Received_Year",\
            SUM(T2."Number_of_individuals_received_pre-test_counseling/information")"Number_of_individuals_received_pre-test_counseling/information",\
            SUM(T2."Number_of_individuals_receiving_post-test_counseling_and_given_results")"Number_of_individuals_receiving_post-test_counseling_and_given_results",\
            SUM(T2."Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling")"Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling",\
            SUM(T3."Number_of_individuals_tested_for_HIV")"Number_of_individuals_tested_for_HIV",\
            SUM(T4."Number_of_individuals_received_result_within_7_days_of_HIV_Test")"Number_of_individuals_received_result_within_7_days_of_HIV_Test",\
            SUM(T5."Number_of_HIV_positive_individuals_having_HIV-I_infection")"Number_of_HIV_positive_individuals_having_HIV-I_infection",\
            SUM(T5."Number_of_HIV_positive_individuals_having_HIV-II_infection")"Number_of_HIV_positive_individuals_having_HIV-II_infection",\
            SUM(T5."Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections")"Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections",\
            SUM(T6."Number_of_individuals_tested_for_HIV_and_found_Negative")"Number_of_individuals_tested_for_HIV_and_found_Negative",\
            SUM(T7."Number_of_Self-initiated_Individuals_tested_for_HIV")"Number_of_Self-initiated_Individuals_tested_for_HIV",\
            SUM(T8."Number_of_Self-initiated_individuals_diagnosed_HIV_positive")"Number_of_Self-initiated_individuals_diagnosed_HIV_positive",\
            SUM(T9."Number_of_provider_initiated_Individuals_tested_for_HIV")"Number_of_provider_initiated_Individuals_tested_for_HIV",\
            SUM(T10."Number_of_provider_initiated_individuals_diagnosed_HIV_positive")"Number_of_provider_initiated_individuals_diagnosed_HIV_positive",\
            SUM(T11."Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC")"Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC"\
            from(\
            select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            case When iv.BENEFICIARY_STATUS=1 Then \
            (cast(count(iben.BENEFICIARY_ID)as numeric)) Else 0 End as "Number_of_individuals_received_pre-test_counseling/information",\
            case When iv.BENEFICIARY_STATUS=4 Then \
            (cast(count(iben.BENEFICIARY_ID)as numeric)) Else 0 End as "Number_of_individuals_receiving_post-test_counseling_and_given_results",\
            case When iv.BENEFICIARY_STATUS=5 Then \
            (cast(count(iben.BENEFICIARY_ID)as numeric)) Else 0 End as "Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling",\
            \
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and \
            iv.BENEFICIARY_STATUS in (1,4,5)\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"' \
            and f.is_active = '"'true'"' \
            and f_sacs.is_active = '"'true'"' \
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"' \
            and ft.is_active = '"'true'"' \
            group by\
            f.id, b.gender,f_sacs.name,f_sacs.id,\
            f.name,iv.BENEFICIARY_STATUS,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date))T2\
            \
            full outer join(\
            select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric) as "Number_of_individuals_tested_for_HIV",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and itr.tested_date is not null\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,\
            b.gender,f_sacs.name,f_sacs.id,\
            f.name,iv.BENEFICIARY_STATUS,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date))T3 on (T2.ID=T3.ID and T2."SACS_ID"=T3."SACS_ID" and T2."Received_Month"=T3."Received_Month" and T2."Received_Year"=T3."Received_Year")\
            full outer join \
            (select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric)as "Number_of_individuals_received_result_within_7_days_of_HIV_Test",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and itr.tested_date is not null\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and cast((cast(isc.sample_collection_date AS DATE) - cast(itr.report_received_date AS DATE))day as numeric) <=7\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),isc.sample_collection_date,\
            itr.report_received_date\
            )T4 on (T2.ID=T4.ID and T2."SACS_ID"=T4."SACS_ID" and T2."Received_Month"=T4."Received_Month" and T2."Received_Year"=T4."Received_Year")\
            \
            full outer join (\
            select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            \
            Case When itr.hiv_type=1 then (cast(count(iben.BENEFICIARY_ID)as numeric))Else 0 End as  "Number_of_HIV_positive_individuals_having_HIV-I_infection",\
            Case When itr.hiv_type=2 then (cast(count(iben.BENEFICIARY_ID)as numeric))Else 0 End as "Number_of_HIV_positive_individuals_having_HIV-II_infection",\
            Case When itr.hiv_type=3 then (cast(count(iben.BENEFICIARY_ID)as numeric))Else 0 End as "Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections",\
            \
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and itr.hiv_type in (1,2,3)\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by \
            f.id,b.gender,f_sacs.name,f_sacs.id,\
            f.name,iv.BENEFICIARY_STATUS,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T5 on (T2.ID=T5.ID and T2."SACS_ID"=T5."SACS_ID" and T2."Received_Month"=T5."Received_Month" and T2."Received_Year"=T5."Received_Year")\
            \
            full outer join \
            (select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            Case When itr.hiv_status=1 then (cast(count(iben.BENEFICIARY_ID)as numeric))Else 0 End  as   "Number_of_individuals_tested_for_HIV_and_found_Negative",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and itr.hiv_status in (1)\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,itr.hiv_status,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T6 on (T2.ID=T6.ID and T2."SACS_ID"=T6."SACS_ID" and T2."Received_Month"=T6."Received_Month" and T2."Received_Year"=T6."Received_Year")\
            \
            full outer join (\
            select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric) as "Number_of_Self-initiated_Individuals_tested_for_HIV",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and iben.referred_by is null\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"' \
            group by\
            f.id,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T7 on (T2.ID=T7.ID and T2."SACS_ID"=T7."SACS_ID" and T2."Received_Month"=T7."Received_Month" and T2."Received_Year"=T7."Received_Year")\
            \
            full outer join (select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric) as "Number_of_Self-initiated_individuals_diagnosed_HIV_positive",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and iben.referred_by is null and itr.hiv_status in (1)\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T8 on (T2.ID=T8.ID and T2."SACS_ID"=T8."SACS_ID" and T2."Received_Month"=T8."Received_Month" and T2."Received_Year"=T8."Received_Year")\
            \
            full outer join \
            (select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric) as "Number_of_provider_initiated_Individuals_tested_for_HIV",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and iben.referred_by is not null\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T9 on (T2.ID=T9.ID and T2."SACS_ID"=T9."SACS_ID" and T2."Received_Month"=T9."Received_Month" and T2."Received_Year"=T9."Received_Year")\
            full outer join \
            (select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric) as "Number_of_provider_initiated_individuals_diagnosed_HIV_positive",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (11,13) and f_sacs.facility_type_id in (2) and iben.referred_by is not null and itr.hiv_status in (1)\
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T10 on (T2.ID=T10.ID and T2."SACS_ID"=T10."SACS_ID" and T2."Received_Month"=T10."Received_Month" and T2."Received_Year"=T10."Received_Year")\
            full outer join \
            (select \
            f.ID, \
            f_sacs.name as "SACS",\
            f.name as "ICTC_center",\
            f_sacs.id as "SACS_ID",\
            cast(count(iben.BENEFICIARY_ID)as numeric) as "Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC",\
            extract(month from iben.registration_date) as "Received_Month",\
            extract(year from iben.registration_date) as "Received_Year"\
            FROM ICTC_BENEFICIARY as iben \
            JOIN BENEFICIARY as b on (iben.BENEFICIARY_ID = b.ID)\
            JOIN ICTC_SAMPLE_COLLECTION as isc on (iben.ID = isc.ICTC_BENEFICIARY_ID)\
            JOIN FACILITY as f on (iben.FACILITY_ID = f.ID)\
            JOIN FACILITY as f_sacs on (f_sacs.id=f.sacs_id)\
            JOIN ICTC_VISIT as iv on (isc.VISIT_ID = iv.ID)\
            JOIN FACILITY_TYPE as ft on (f.FACILITY_TYPE_ID = ft.ID)\
            JOIN ICTC_TEST_RESULT as itr on (iv.ID = itr.VISIT_ID)\
            where f.facility_type_id in (10,11,13) and f_sacs.facility_type_id in (2) and itr.hiv_status in (3) \
            and iv.IS_PREGNANT = '"'true'"'\
            and b.gender in ('"'female'"')\
            and iben.is_active = '"'true'"'\
            and b.is_active = '"'true'"' \
            and isc.is_active = '"'true'"'\
            and f.is_active = '"'true'"'\
            and f_sacs.is_active = '"'true'"'\
            and iv.is_active = '"'true'"' \
            and itr.is_active = '"'true'"'\
            and ft.is_active = '"'true'"'\
            group by\
            f.id,b.gender,\
            f.name,iv.BENEFICIARY_STATUS,f_sacs.name,f_sacs.id,\
            extract(month from iben.registration_date),\
            extract(year from iben.registration_date),itr.hiv_type)T11 \
            on (T2.ID=T11.ID and T2."SACS_ID"=T11."SACS_ID" and T2."Received_Month"=T11."Received_Month" and T2."Received_Year"=T11."Received_Year")\
            group by \
            T2.ID,\
            T2."SACS",\
            T2."ICTC_center",\
            T2."SACS_ID",\
            T2."Received_Month",\
            T2."Received_Year"\
            \
            )table2\
            group by\
            table2."SACS_ID" ,\
            table2."SACS",\
            table2."Received_Month",	\
            table2."Received_Year" \
            )table3\
            group by \
            \
            table3."Received_Month",	\
            table3."Received_Year"'
    #Execute query
    xl_df = pd.read_sql(sql, conn.connect())
    return xl_df

def create_report():
    #Get dataframe
    df = fetch_data()
    # Start by opening the spreadsheet and selecting the main sheet
    workbook = load_workbook(filename='templates\\ictc_report_section_i_template.xlsx')
    sheet = workbook.active
    
    #Check if DF is empty
    if df.empty:
        print('DataFrame is empty!')
    else:# Write what you want into a specific cell
        print(df)
        sheet["H9"] = df['Number_of_individuals_received_pre-test_counseling/information']
        sheet["H10"] = df['Number_of_individuals_tested_for_HIV']
        sheet["H11"] = df['Number_of_individuals_receiving_post-test_counseling_and_given_results']
        sheet["H12"] = df['Number_of_individuals_received_result_within_7_days_of_HIV_Test']        
        sheet["H13"] = 0 # once mapping available, update it.
        sheet["H14"] = df['Number_of_HIV_positive_individuals_having_HIV-I_infection']
        sheet["H15"] = df['Number_of_HIV_positive_individuals_having_HIV-II_infection']
        sheet["H16"] = df['Number_of_HIV_positive_individuals_having_both_HIV-I_&_II_infections']
        sheet["H17"] = df['Number_of_individuals_tested_for_HIV_and_found_Negative']
        sheet["H18"] = df['Number_of_individuals_with_High_Risk_Behavior_received_follow-up_counseling']
        sheet["H19"] = df['Number_of_Self-initiated_Individuals_tested_for_HIV']
        sheet["H20"] = df['Number_of_Self-initiated_individuals_diagnosed_HIV_positive']
        sheet["H21"] = df['Number_of_provider_initiated_Individuals_tested_for_HIV']
        sheet["H22"] = df['Number_of_provider_initiated_individuals_diagnosed_HIV_positive']
        sheet["H123"] = df['Total_number_of_individuals_turned_Indeterminate_for_HIV_at_SA_ICTC']

    # Save the spreadsheet
    now = datetime.datetime.now()
    pref = now.strftime('%Y_%b_')
    workbook.save(filename='reports\\ictc_report_' + pref + '_section_i national pregnant.xlsx')
    print ('*** Excel report created.')

# Test the Function        
if __name__=="__main__":
    create_report()
