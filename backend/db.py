import mysql.connector #MYQSL iig python tai holbogdoh bolmjtoi bolgoh toolyg importloj bn
def get_connection(): # get_connection function iig todorhoilj database tei holboh uregtei back endiin buh hesegt datag ashyglah guur boln
    return mysql.connector.connect( # mysql tai holbogdsnii daraa ymr erh haana ymr data ashyglah geh met zuilyg zaah function
        host="localhost", # mysql ni minii computer oos ajylj bgag zaana
        user="root", # root erher buyu admin erher handah buhii l uurchlult hiih bolmj ugnu
        password="Frost0526@",# minii mysql iin password
        database="crud_project" # mysql dotorh aly database iig ashyglah ner
    )
