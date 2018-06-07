import Tkinter, time
BatteryStatsWindowMain = Tkinter.Tk()
BatteryStatsWindowMain.title("Battery Meter Simulator")
BatteryStatsWindow = Tkinter.Frame(BatteryStatsWindowMain, highlightthickness = 10, highlightbackground = "white")
BatteryStatsWindow.pack()
BatteryLifeFrame = Tkinter.Frame(BatteryStatsWindow)
BatteryConfigFrame = Tkinter.Frame(BatteryStatsWindow)
BatteryConfigSubFrameState = Tkinter.Frame(BatteryConfigFrame)
BatteryConfigSubFrame1 = Tkinter.Frame(BatteryConfigFrame)
BatteryConfigSubFrame2 = Tkinter.Frame(BatteryConfigFrame)
BatteryConfigSubFrame3 = Tkinter.Frame(BatteryConfigFrame)
BatteryLife = 6
BatteryPower = 100
class BatteryMeter:
	def __init__(self):
		self.MeterCanvas = Tkinter.Canvas(BatteryLifeFrame, width = 108, height = 184, border = 0, highlightbackground = "black", highlightthickness = 1)
		self.CurrentBatteryPower = BatteryPower
		self.id = self.MeterCanvas.create_rectangle(0, 184 - self.CurrentBatteryPower * 2, 108, 184, fill = "green")
		self.MeterCanvas.pack()
		self.Time = time.time()
		self.PercentLabel = Tkinter.Label(BatteryLifeFrame, text = "%s%% Remaining" % self.CurrentBatteryPower)
		self.PercentLabel.pack()
		self.BatteryLife = BatteryLife
		self.ChargeSpeed = 4
		self.Charge = Tkinter.StringVar()
		self.UsedBatteryPercent = 100 / (((self.BatteryLife * 60) * 60) / (time.time() - self.Time))
		self.ChargedPercent = 100 / (((self.ChargeSpeed * 60) * 60) / (time.time() - self.Time))
	def DischargeBattery(self):
		self.MeterCanvas.delete(self.id)
		if self.CurrentBatteryPower != 0 and self.Charge.get() == "Use" and self.UsedBatteryPercent >= 1:
			self.CurrentBatteryPower -= 1
		elif self.CurrentBatteryPower != 100 and self.Charge.get() == "Charge" and self.ChargedPercent >= 1:
			self.CurrentBatteryPower += 1
			print self.ChargedPercent
		self.id = self.MeterCanvas.create_rectangle(0, 184 - self.CurrentBatteryPower * 2, 108, 184, fill = "green")
		self.PercentLabel.destroy()
		self.PercentLabel = Tkinter.Label(BatteryLifeFrame, text = "%s%% Remaining" % self.CurrentBatteryPower)
		self.PercentLabel.pack()
		self.Time = time.time()
	def NumberBox(self, Frame):
		return Tkinter.Spinbox(Frame, width = 4, from_ = 0, to = 100)
	def ConfigBattery(self):
		BatteryPower = int(PercentFull.get())
		self.BatteryLife = float(AvgHours.get())
		self.CurrentBatteryPower = BatteryPower
		self.ChargeSpeed = float(AvgChargeHours.get())
batteryMeter = BatteryMeter()
BatteryLifeFrame.pack(side = "left")
Tkinter.Label(BatteryConfigSubFrameState, text = "Battery State").pack(side = "left")
PercentFull = Tkinter.OptionMenu(BatteryConfigSubFrameState, batteryMeter.Charge, "Use", "Charge", "Standby")
PercentFull.pack(side = "right")
Tkinter.Label(BatteryConfigSubFrame1, text = "% Full").pack(side = "left")
PercentFull = batteryMeter.NumberBox(BatteryConfigSubFrame1)
PercentFull.pack(side = "right")
Tkinter.Label(BatteryConfigSubFrame2, text = "Battery Life").pack(side = "left")
AvgHours = batteryMeter.NumberBox(BatteryConfigSubFrame2)
AvgHours.pack(side = "right")
Tkinter.Label(BatteryConfigSubFrame3, text = "Charge Speed").pack(side = "left")
AvgChargeHours = batteryMeter.NumberBox(BatteryConfigSubFrame3)
AvgChargeHours.pack(side = "right")
BatteryConfigSubFrameState.pack()
BatteryConfigSubFrame1.pack()
BatteryConfigSubFrame2.pack()
BatteryConfigSubFrame3.pack()
ChangeConfigs = Tkinter.Button(BatteryConfigFrame, text = "Simulate Battery", command = batteryMeter.ConfigBattery)
ChangeConfigs.pack()
Tkinter.Frame(BatteryStatsWindow, width = 10).pack(side = "left")
BatteryConfigFrame.pack(side = "left")
while True:
	try:
		batteryMeter.UsedBatteryPercent = 100 / (((batteryMeter.BatteryLife * 60) * 60) / (time.time() - batteryMeter.Time))
		batteryMeter.ChargedPercent = 100 / (((batteryMeter.ChargeSpeed * 60) * 60) / (time.time() - batteryMeter.Time))
		if batteryMeter.UsedBatteryPercent >= 1 or batteryMeter.ChargedPercent >= 1:
			batteryMeter.DischargeBattery()
	except ZeroDivisionError:
		batteryMeter.BatteryLife = 0.001
		batteryMeter.ChargeSpeed = 0.001
	BatteryStatsWindow.update_idletasks()
	BatteryStatsWindow.update()
Tkinter.mainloop()