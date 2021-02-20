import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import webbrowser
import dash_enterprise_auth as auth
import os
from secrets import *
import secrets
import hashlib
import json
import requests
from dash.dependencies import Input, Output, State
import pymongo
import dash_bootstrap_components as dbc
from flask_caching import Cache



#lis=[]



data = pd.read_json("cache-directory/ex.json")
print(data)
print(data["data"]["sortdata"])

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },

]
app = dash.Dash(__name__, external_stylesheets=[external_stylesheets,dbc.themes.BOOTSTRAP])





app.title = "SonarQube-UI-Analytics"

################################################### partie de navigate.py
a=hashlib.sha256(secrets.token_urlsafe(16).encode('utf-8')).hexdigest()
f=open("cache-directory/sortdata.json")
d1 = json.load(f)
d = pd.DataFrame(d1)

def generate(id_n):
    return html.Button(dcc.Link(str(id_n), href="http://localhost:8050/"+str(id_n)+"/"+'?token='+str(a)+"#rules"))


def make_card(id_name,val):
    return html.Div([
        html.Div([
            html.Div([
                (html.A(str(d[str(val)]['data'][id_name]['src']), href='localhost:9000/project/issues?id=ecomanif&languages=py&open=AXcqnocF-n2LilEsa22c&resolved=false&types=BUG', target='_blank',className = 'boxHeader')),
                dcc.Checklist(
                    id=str(id_name),
                    options=[
        {'label': 'FP', 'value': '1'}
    ],
    value=[]),
                html.Div( className = 'boxNumbers')
            ], className = 'boxText')
                    ], className = 'innerBox' ),
            html.Br(),
    ], className='cardb', id=str(id_name))
divs = []


def hello(k):
    for id_name in range(len(d[str(k.replace('/',''))]['data'])) :
        divs.append(make_card(id_name,str(k.replace('/',''))))
    return divs

##################################


table_header = [
    html.Thead(html.Tr([html.Th("SonarQube FP"), html.Th("Solved"),html.Th("Commentaire")]))
]

row1 = html.Tr([html.Td(html.Img(src="/assets/dict.png")), html.Td(html.Img(src="/assets/dict_solved.png")),html.Td("Remplacer par {**d1, **d2} ")])
row2 = html.Tr([html.Td(html.Img(src="/assets/encryption.png")), html.Td(html.Img(src="/assets/encryption_solved.png")),html.Td()])
row3 = html.Tr([html.Td(html.Img(src="/assets/zip.png")), html.Td(html.Img(src="/assets/zip_solved.png")),html.Td("Utiliser la librairie shutil")])
row4 = html.Tr([html.Td(html.Img(src="/assets/nan.png")), html.Td(html.Img(src="/assets/nan_solved.png")),html.Td("Utiliser la librairie math")])
row5 = html.Tr([html.Td(html.Img(src="/assets/hash.png")), html.Td(html.Img(src="/assets/hash1.png")),html.Td("Remplacer is par != et ajouter un commentaire")])
row6 = html.Tr([html.Td(html.Img(src="/assets/string.png")), html.Td(children=[html.Img(src="/assets/fstringsolv.png"),html.Img(src="/assets/fstringsolv2.png")]),html.Td(children=[html.Div("1/ Création d’une fonction contenant la variable x. Puis l’insérer dans le f_string de la fonction principale. "),html.Div("2/ Déclarer la variable comme constante dans l’argument de la fonction ")])])
row7 = html.Tr([html.Td(html.Img(src="/assets/import.png")), html.Td(html.Img(src="/assets/importsolv.png")),html.Td()])
row8 = html.Tr([html.Td(html.Img(src="/assets/read.png")), html.Td(html.Img(src="/assets/readsolv.png")),html.Td()])
row9 = html.Tr([html.Td(html.Img(src="/assets/comment.png")), html.Td(html.Img(src="/assets/commentsolv.png")),html.Td("Rajouter un commentaire dans la fonction")])
link= html.A("https://jira.sonarsource.com/projects/SONARPY/issues",href='https://jira.sonarsource.com/projects/SONARPY/issues', target='_blank')

table_body = [html.Tbody([row1, row2, row3, row4,row5,row6,row7,row8,row9,link])]

table= dbc.Table(table_header + table_body, bordered=True)

#######################################################
table_header2 = [
    html.Thead(html.Tr([html.Th("Catégorie"), html.Th("Vulnérabilité"),html.Th("Solved")]))
]


row2_2 = html.Tr([html.Td("Hachage "),html.Td(html.Img(src="/assets/size/hachage_vul.png")), html.Td(html.Img(src="/assets/hachage_solv.png"))])
row2_3 = html.Tr([html.Td("Random JS "),html.Td("Math.random() "), html.Td(html.Img(src="/assets/crypto.png"))])
row2_4 = html.Tr([html.Td("Random Python "),html.Td("random.randint(1,99999) "), html.Td(html.Img(src="/assets/secret.png"))])
row2_5 = html.Tr([html.Td("Random avec choice "),html.Td("random.choice(string.ascii_uppercase + string.digits)"), html.Td("secrets.choice(string.ascii_uppercase + string.digits) ")])
row2_6 = html.Tr([html.Td("RegExp JS "),html.Td("regular expression engines "), html.Td("Use npm re2 ")])
row2_7 = html.Tr([html.Td("TLS "),html.Td("response = requests.get(login_url, verify=False) "), html.Td(html.Img(src="/assets/size/tls.png"))])

table_body2 = [html.Tbody([ row2_2, row2_3, row2_4,row2_5,row2_6,row2_7])]

table2= dbc.Table(table_header2 + table_body2, bordered=True)

##################################Documentation
documentation=html.Div(children=[html.H1("Modifier une règle dans SonarQube"),
    html.Br(),html.Div("Intro: Cloner le répertoire Sonar-Python: git clone https://github.com/SonarSource/sonar-python.git"),html.Br(),
    html.H3("3 élèments à utiliser"),html.Br(),
    html.P("0/ On prend par exemple la règle initReturnsValue"),
    html.Br(),
    html.Img(src="/assets/rules.png"),
    html.Br(),
    html.P(),
    html.Br(),
    html.H5("1/ La partie Python: path=sonar-python/python-checks/src/test/resources/checks/initReturnsValue.py"),
    html.Br(),
    html.Img(src="/assets/pyjava.png"),
    html.Br(),
    html.Br(),
    html.P("l'encadré en vert correspond au code python qui doit compiler et qui n'envoie pas d'erreur"),
    html.P("l'encadré en rouge correspond au code python qui ne doit compiler et envoie une erreur"),
    html.Br(),
    html.H5("2/ La partie Check: path=sonar-python/python-checks/src/main/java/org/sonar/python/checks/InitReturnsValueCheck.java"),
    html.Br(),
    html.Img(src="/assets/check.PNG"),
    html.Br(),
    html.P(),
    html.Br(),
    html.H5("3/ La partie Test: path=sonar-python/python-checks/src/test/java/org/sonar/python/checks/InitReturnsValueCheckTest.java"),
    html.Br(),
    html.Img(src="/assets/test.PNG"),
    html.Br(),
    html.P(),
    html.Br(),
    html.P("click droit>Run As>JUnit Test"),
    html.Br(),
    html.Img(src="/assets/solved.PNG"),
    html.Br(),
    html.H3("On compile"),
    html.Br(),
    html.Img(src="/assets/mvnpackage.PNG"),
    html.Br(),
    html.Br(),
    html.Img(src="/assets/success.PNG"),
    html.Br(),
    html.Br(),
    html.Img(src="/assets/plugin.PNG"),
    html.Br(),
    html.H3("On Intègre"),
    html.Br(),
    
    html.Br(),
    html.P("Path=sonarqube-8.5.1.38104/lib/extensions"),
    html.Br(),
    html.Img(src="/assets/it.PNG"),
    html.Br(),
    html.P(),
     html.Br(),
    html.Img(src="/assets/qualité.PNG"),
    html.Br(),
    html.Br(),
    html.Img(src="/assets/newprofil.PNG"),
    html.Br(),
    html.Br(),
    html.Img(src="/assets/bulk.PNG"),
    html.Br(),
    html.Br(),
    html.Img(src="/assets/applique.PNG"),
    html.Br(),
    html.Br(),
    html.Img(src="/assets/fin.PNG"),
    html.Br(),
    html.P("On définit la nouvelle règle par défaut"),
    html.Br(),






    ])


##############################


def items(i,name,data):
    # we use this function to make the example items to avoid code duplication
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        name,
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(data),
                id=f"collapse-{i}",
            ),
        ]
    )

######################################################

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📡", className="header-emoji"),
                html.H1(
                    children="SonarQube-UI-Analytics", className="header-title"
                ),

                html.P(
                    children="Analyseur de Faux Positif",
                    className="header-description",
                ),
                ####################################dropdown
                html.Div([
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem(
                                    "Règles", href="http://localhost:8050/#rules"
                                ),
                                dbc.DropdownMenuItem(
                                    "Wiki", href="http://localhost:8050/#group-1-toggle",target="_self",
                                ),
                                dbc.DropdownMenuItem(
                                    "Sécurité", href="http://localhost:8050/#group-2-toggle",target="_self",
                                ),
                                dbc.DropdownMenuItem(
                                    "Documentation", href="http://localhost:8050/#group-3-toggle",target="_self",
                                ),
                            ],
                            label="📡",id="dropdown"
                        ),
                        html.P(id="item-clicks", className="mt-3"),
                    ]
                ),
            ],
            className="header",
        ),
        

        





        html.Div(
            children=[

                html.Div(children=dcc.Graph(id='exemple',
                    config={"displayModeBar": False},
                    figure={
                    'data':[
                        {'x':['rawdata','data','sortdata'],'y':[data["data"]["rawdata"],data["data"]["data"],data["data"]["sortdata"]],'type':'bar','name':'line_code','marker' : { "color" : ["red","orange","green"]}},
                        {'x':["false_positive"],'y':[data["data"]["false_positive"]],'type':'bar','name':'faux_positif','marker' : { "color" : ["black"]}},
                        {'x':['duplicate_rate_error'],'y':[(data["data"]["sortdata"]/data["data"]["data"])*100],'type':'bar','name':'percentage','marker' : { "color" : ["blue"]}},
                        {'x':["rules"],'y':[data["data"]["rules"]],'type':'bar','name':'rules','marker' : { "color" : ["brown"]}},
                    ],
                    'layout':{
                        'title':'Information Générale'
                        },


                    }),className="card",


               ),
                ##########"carousel"
                html.A(html.Button('Refresh Data'),href='/'),        

                html.Br(),html.Br(),html.Br(),
                html.Div([


                ]),


              
               

                # content will be rendered in this element

                 html.Div(id='display'),
                 dcc.Location(id='url', refresh=False),
                 html.Div(
                 html.Div(children=[ generate(i)  for i in d ] ,id="rules"),className="card2"),
                 html.Div(id='page-content'),

                 html.Div([items(1,"Wiki",table), items(2,"Sécurité",table2),items(3,"Documentation",documentation)], className="accordion"),
                

                 
            
                ###############graph

            ],
            className="wrapper",
        ),
        ############""
        
        ###################
        html.Div(
            children=[
                html.H3(
                    children="OPENSCOP", className="font",
                )
            ],
            className="footer",
        ),
    ]
)

###############################partie2 de navigate.py
ele=[]
#print(divs)
##############################


#app.config.suppress_callback_exceptions = True

##################################calback
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])


def display_page(pathname):
    ele.append(pathname)
    if len(ele) > 1:
        divs.clear()

    hello(pathname)

    




    return html.Div([
        html.H3('Rule: {}'.format(pathname)),
        html.Div(children=["❔",html.Span('The __init__ method is required to return None. A TypeError will be raised if the __init__ method either yields or returns any expression other than None. Returning some expression that evaluates to None will not raise an error, but is considered bad practice.',className='tooltiptext')],className='tooltip'),
        html.Div(divs, className='card'),

    ])


#########################multiple

@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(1, 4)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 4)],
    [State(f"collapse-{i}", "is_open") for i in range(1, 4)],
)
def toggle_accordion(n1, n2,n3, is_open1, is_open2,is_open3):
    ctx = dash.callback_context
    print(ctx.triggered)
    if not ctx.triggered:
        return False, False,False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        print(button_id)

    if button_id == "group-1-toggle" and n1:
        return not is_open1, False,False
    elif button_id == "group-2-toggle" and n2:
        return False, not is_open2, False
    elif button_id == "group-3-toggle" and n3:
        return False, False, not is_open3
    return False, False,False


##############single accordéon
'''
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

'''

def glob(path):
    ele.append(path)
    global g
    g=ele
    if len(g)>1:

        g =ele[-1]
    return g



@app.callback(dash.dependencies.Output('page', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def ur(pathname):
    global dat
    dat=glob(pathname)
    return (dat)
    
 
    ##############################""


@app.callback(Output('display', 'children'),dash.dependencies.Input('url', 'pathname'),[Input(str(i), "value") for i in range(5)],)

def set_display_children(*argv):
    lis=[]
    ctx = dash.callback_context
    for arg in argv:
        lis.append(arg) 
        print(ctx.triggered)

            #li.append(s)
            #li.append(k)
    print(lis)


################################""
if __name__ == "__main__":
    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open_new('http://localhost:8050')
    app.run_server(debug=False)
    
    