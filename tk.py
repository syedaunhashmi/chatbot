import chatterbot
import pickle
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import os
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time


class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
            "GUI Bot",

            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[{
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.80
} ]



        )


        corpus_trainer = ChatterBotCorpusTrainer(self.chatbot)
        corpus_trainer.train('chatterbot.corpus.english')
        self.title("Chatterbot")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        style = ttk.Style()
        style.map("C.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')]
            )


        self.respond = ttk.Button(self, text='Get Response',cursor='hand2' ,command=self.get_response)
        self.respond.grid(column=1, row=2, sticky='nesw', padx=3, pady=10)




        self.usr_input = tk.Entry(self, state='normal',text='Enter your query here!')
        self.usr_input.grid(column=0, row=2, sticky='nesw', padx=1, pady=5)

        #Binding entry
        self.usr_input.bind('<Return>',self.get_response)


        self.conversation_lbl = tk.Label(self,
                                         text='English',
                                         anchor='center',
                                         font=('Arial Bold ',18),
                                         bg="#3a8fc5",
                                         fg="white")
        self.conversation_lbl.grid(column=0, row=0,columnspan=2, padx=3, pady=3,sticky='news')
        self.conversation = ScrolledText.ScrolledText(self,
                                                      state='disabled',borderwidth=5,
                                                      highlightthickness=1,
                                                      bg='#15202b',fg='#16202A',
                                                      font=('Arial Bold',8))

        self.conversation.grid(column=0, row=1, columnspan=2, sticky='nesw', padx=3, pady=3)


    def get_response(self,*args):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)

        self.conversation['state'] = 'normal'
        '''----------------------------------------------
        self.conversation.tag_configure('tag-left', justify='left')
        self.conversation.insert('end',"Human: " + user_input + "\n", 'tag-left')

        self.conversation.tag_configure('tag-left', justify='right')
        self.conversation.insert('end',"ChatBot: " + str(response.text) + "\n\n\n", 'tag-right')'''

        label1 = tk.Label(self.conversation, 
                          text="Human: \n"+user_input, 
                          background='#3B5566',
                          fg='white',
                          font=("Helvetica", 12),
                          justify='left',
                          wraplength=300,
                          anchor='w',
                          padx=10, pady=5)
        label2 = tk.Label(self.conversation, 
                          text="ChatBot: \n"+str(response.text),
                          wraplength=300,
                          anchor='w',
                          background='#1D9DFC', 
                          fg='white',
                          font=("Helvetica", 12),
                          justify='left',
                          padx=10, pady=5)

        self.conversation.tag_configure('tag-left', justify='left')
        self.conversation.tag_configure('tag-right', justify='right')


        self.conversation.insert('end', '\n\n\n')
        self.conversation.window_create('end', window=label1)

        self.conversation.insert('end', '\n\n\n ', 'tag-right') # space to move Label to the right 
        self.conversation.window_create('end', window=label2)

        '''self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n\n\n"
        )'''
        self.conversation['state'] = 'disabled'

        time.sleep(0.2)

gui_example = TkinterGUIExample()
gui_example.attributes('-topmost', True)
gui_example.update()
gui_example.attributes('-topmost', False)
gui_example.geometry('810x550+460+100')
gui_example.resizable(0, 0)
gui_example.configure(background='#3a8fc5')
gui_example.mainloop()