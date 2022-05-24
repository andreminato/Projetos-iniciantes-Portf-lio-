import win32com.client as win32

#criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

#criar um email
email = outlook.CreateItem(0)

v1 = Latum 
v2 = Sensum 
info = pyautogui

#configurar as informações do email
email.To = 'aminato40@outlook.com; jose@bol.com'
email.Subject = 'Email automático do André'
email.HTMLBody = f'<p> O texto aqui pode ser formatato conforme a necessidade </p>'
'<p> As variáveris {v1, v2} podem ser informações extraídas de algum BD ou arquivo. <p>'
'<p> Também tem a possibilidade de automatizar o processo de downloado dos dados com a extensão {pyautogui} </p>'

email.Send()
print('Email enviado')


