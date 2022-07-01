import Quete

class NPC():
    def __init__(self, pName, pBasicDialog, pFunction='@'):
        self.name = pName
        self.dialogues = []
        self.quests = []
        self.idleDialog = pBasicDialog
        self.function = pFunction
        
    def linkQuest(self, pQuestId, pDialogList):
        self.quests.append(pQuestId)
        self.dialogues.append(pDialogList)

    # def talk(self):
    #     LastFinishedQuestId=-1
    #     for i in range(self.quests):
    #         if ListeQuete[int(self.quests[i])].Etat=="Reussie":
    #             LastFinishedQuestId=i
    #     if LastFinishedQuestId+1==len(self.quests):
    #         dialogue(self.dialogues[LastFinishedQuestId+1][2])
    #     else:
    #         if ListeQuete[int(self.quests[LastFinishedQuestId+1])].Etat=="Invisible":
    #             dialogue(self.dialogues[LastFinishedQuestId+1][0])
    #             ListeQuete[int(self.quests[LastFinishedQuestId+1])].Etat=="En cours"
    #         elif ListeQuete[int(self.quests[LastFinishedQuestId+1])].Etat=="En cours":
    #             validation(int(liste(LastFinishedQuestId+1)))
    #             if ListeQuete[int(self.quests[LastFinishedQuestId+1])].Etat=="En cours":
    #                 dialogue(self.dialogues[LastFinishedQuestId+1][1])
    #             elif ListeQuete[int(self.quests[LastFinishedQuestId+1])].Etat=="Reussie":
    #                 dialogue(self.dialogues[LastFinishedQuestId+1][2])
    #                 ListeQuete[int(self.quests[LastFinishedQuestId+1])].Etat=="En cours"


def iniNPCs():
    dictNPC = {}
    dictNPC['t'] = NPC( 'Quincalllerie', "J'ai (presque) ce qu'il te faut", 'self.menu.openCompTrade()')
    dictNPC['s'] = NPC( 'Excelinator', 'Regardons plus précisément tes moyennes...', 'self.menu.openSkillsEquipement()')
    dictNPC['r'] = NPC( 'Infirmière', ['Tu as été soigné','Fais attention la prochaine fois'],'self.player.addHp(self.player.hpMax)')
    return dictNPC
        