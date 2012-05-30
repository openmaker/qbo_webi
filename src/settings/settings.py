# coding: utf-8
import cherrypy
import os
import glob
from mako.template import Template
from tabsClass import TabClass
import rospy

class SettingsManager(TabClass):
    
    def __init__(self,language):
        self.language = language
        self.htmlTemplate = Template(filename='settings/templates/settingsTemplate.html')
        self.languages_names={'en':'English','es':'Español','pt':'Português','de':'Deutsch','fr':'Français','it':'Italiano'}

    def get_languages(self):
#        dirList=os.listdir("lang")
#        os.chdir("lang")
        langlist=[]
#        for fname in langlist.glob("*.txt"):
        for fname in glob.glob("lang/*.txt"):
            langlist.append(fname[5:-4])
        langlist.sort()
        print langlist
        return langlist


    @cherrypy.expose
    def index(self):
        all_lang=self.get_languages()
        return self.htmlTemplate.render(language=self.language,lannames=self.languages_names,alllanguage=all_lang)


