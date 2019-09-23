import wx

class SimpleApp(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title)
		self.parent = parent
		self.initialize()

	def initialize(self):
		sizer = wx.GridBagSizer()
		
		self.entry = wx.TextCtrl(self, -1, value=u'Enter text here:')
		sizer.Add(self.entry, (0,0),(1,1), wx.EXPAND)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

		button = wx.Button(self, -1, label='click Me!')
		sizer.Add(button, (0,1))
		self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)

		self.label= wx.StaticText(self, -1, label=u'Hello')
		self.label.SetBackgroundColour(wx.BLUE)
		self.label.SetForegroundColour(wx.WHITE)
		sizer.Add(self.label,(1,0),(1,2),wx.EXPAND)

		sizer.AddGrowableCol(0)
		self.SetSizerAndFit(sizer)
		self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y) #-1 no limit, GetSize().y limit hight
		self.entry.SetFocus()
		self.entry.SetSelection(-1,-1) # Select all text
		self.Show(True)

	def OnButtonClick(self, event):
		self.label.SetLabel(self.entry.GetValue() + '(You.., You Clicked Me!!)')
		self.entry.SetFocus()
		self.entry.SetSelection(-1,-1)
		# self.label.SetLabel('You, you.. clicked me!')
		print('Clicked, I got Clicked!')

	def OnPressEnter(self, event):
		self.label.SetLabel(self.entry.GetValue() + '(You presses the Enter!)')
		self.entry.SetFocus()
		self.entry.SetSelection(-1,-1)
		# self.label.SetLabel('You Presses the Enter!')
		print('entered the enter')

if __name__ == '__main__':
	'''
		parrent None because there is no parent, 
		-1 let wx make a choice for identifier
		'app...name' Application name
	'''
	app = wx.App()
	frame = SimpleApp(None, -1, 'My Application')
	app.MainLoop()