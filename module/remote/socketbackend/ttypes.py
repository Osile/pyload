#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

class BaseObject(object):
	__slots__ = []

class Destination:
	Collector = 0
	Queue = 1

class DownloadStatus:
	Aborted = 9
	Custom = 11
	Decrypting = 10
	Downloading = 12
	Failed = 8
	Finished = 0
	Offline = 1
	Online = 2
	Processing = 13
	Queued = 3
	Skipped = 4
	Starting = 7
	TempOffline = 6
	Unknown = 14
	Waiting = 5

class ElementType:
	File = 1
	Package = 0

class AccountInfo(BaseObject):
	__slots__ = ['validuntil', 'login', 'options', 'valid', 'trafficleft', 'maxtraffic', 'premium', 'type']

	def init(self, validuntil=None, login=None, options=None, valid=None, trafficleft=None, maxtraffic=None, premium=None, type=None):
		self.validuntil = validuntil
		self.login = login
		self.options = options
		self.valid = valid
		self.trafficleft = trafficleft
		self.maxtraffic = maxtraffic
		self.premium = premium
		self.type = type

class CaptchaTask(BaseObject):
	__slots__ = ['tid', 'data', 'type', 'resultType']

	def init(self, tid=None, data=None, type=None, resultType=None):
		self.tid = tid
		self.data = data
		self.type = type
		self.resultType = resultType

class ConfigItem(BaseObject):
	__slots__ = ['name', 'description', 'value', 'type']

	def init(self, name=None, description=None, value=None, type=None):
		self.name = name
		self.description = description
		self.value = value
		self.type = type

class ConfigSection(BaseObject):
	__slots__ = ['name', 'description', 'items', 'outline']

	def init(self, name=None, description=None, items=None, outline=None):
		self.name = name
		self.description = description
		self.items = items
		self.outline = outline

class DownloadInfo(BaseObject):
	__slots__ = ['fid', 'name', 'speed', 'eta', 'format_eta', 'bleft', 'size', 'format_size', 'percent', 'status', 'statusmsg', 'format_wait', 'wait_until', 'packageID', 'packageName', 'plugin']

	def init(self, fid=None, name=None, speed=None, eta=None, format_eta=None, bleft=None, size=None, format_size=None, percent=None, status=None, statusmsg=None, format_wait=None, wait_until=None, packageID=None, packageName=None, plugin=None):
		self.fid = fid
		self.name = name
		self.speed = speed
		self.eta = eta
		self.format_eta = format_eta
		self.bleft = bleft
		self.size = size
		self.format_size = format_size
		self.percent = percent
		self.status = status
		self.statusmsg = statusmsg
		self.format_wait = format_wait
		self.wait_until = wait_until
		self.packageID = packageID
		self.packageName = packageName
		self.plugin = plugin

class EventInfo(BaseObject):
	__slots__ = ['eventname', 'id', 'type', 'destination']

	def init(self, eventname=None, id=None, type=None, destination=None):
		self.eventname = eventname
		self.id = id
		self.type = type
		self.destination = destination

class FileData(BaseObject):
	__slots__ = ['fid', 'url', 'name', 'plugin', 'size', 'format_size', 'status', 'statusmsg', 'packageID', 'error', 'order']

	def init(self, fid=None, url=None, name=None, plugin=None, size=None, format_size=None, status=None, statusmsg=None, packageID=None, error=None, order=None):
		self.fid = fid
		self.url = url
		self.name = name
		self.plugin = plugin
		self.size = size
		self.format_size = format_size
		self.status = status
		self.statusmsg = statusmsg
		self.packageID = packageID
		self.error = error
		self.order = order

class FileDoesNotExists(Exception):
	__slots__ = ['fid']

	def init(self, fid=None):
		self.fid = fid

class OnlineCheck(BaseObject):
	__slots__ = ['rid', 'data']

	def init(self, rid=None, data=None):
		self.rid = rid
		self.data = data

class OnlineStatus(BaseObject):
	__slots__ = ['name', 'plugin', 'packagename', 'status', 'size']

	def init(self, name=None, plugin=None, packagename=None, status=None, size=None):
		self.name = name
		self.plugin = plugin
		self.packagename = packagename
		self.status = status
		self.size = size

class PackageData(BaseObject):
	__slots__ = ['pid', 'name', 'folder', 'site', 'password', 'dest', 'order', 'linksdone', 'sizedone', 'sizetotal', 'linkstotal', 'links', 'fids']

	def init(self, pid=None, name=None, folder=None, site=None, password=None, dest=None, order=None, linksdone=None, sizedone=None, sizetotal=None, linkstotal=None, links=None, fids=None):
		self.pid = pid
		self.name = name
		self.folder = folder
		self.site = site
		self.password = password
		self.dest = dest
		self.order = order
		self.linksdone = linksdone
		self.sizedone = sizedone
		self.sizetotal = sizetotal
		self.linkstotal = linkstotal
		self.links = links
		self.fids = fids

class PackageDoesNotExists(Exception):
	__slots__ = ['pid']

	def init(self, pid=None):
		self.pid = pid

class ServerStatus(BaseObject):
	__slots__ = ['pause', 'active', 'queue', 'total', 'speed', 'download', 'reconnect']

	def init(self, pause=None, active=None, queue=None, total=None, speed=None, download=None, reconnect=None):
		self.pause = pause
		self.active = active
		self.queue = queue
		self.total = total
		self.speed = speed
		self.download = download
		self.reconnect = reconnect

class ServiceCall(BaseObject):
	__slots__ = ['plugin', 'func', 'arguments', 'parseArguments']

	def init(self, plugin=None, func=None, arguments=None, parseArguments=None):
		self.plugin = plugin
		self.func = func
		self.arguments = arguments
		self.parseArguments = parseArguments

class ServiceDoesNotExists(Exception):
	__slots__ = ['plugin', 'func']

	def init(self, plugin=None, func=None):
		self.plugin = plugin
		self.func = func

class ServiceException(Exception):
	__slots__ = ['msg']

	def init(self, msg=None):
		self.msg = msg

class UserData(BaseObject):
	__slots__ = ['name', 'email', 'role', 'permission', 'templateName']

	def init(self, name=None, email=None, role=None, permission=None, templateName=None):
		self.name = name
		self.email = email
		self.role = role
		self.permission = permission
		self.templateName = templateName

class Iface:
	def addFiles(self, pid, links):
		pass
	def addPackage(self, name, links, dest):
		pass
	def call(self, info):
		pass
	def checkOnlineStatus(self, urls):
		pass
	def checkOnlineStatusContainer(self, urls, filename, data):
		pass
	def checkURLs(self, urls):
		pass
	def deleteFiles(self, fids):
		pass
	def deleteFinished(self):
		pass
	def deletePackages(self, pids):
		pass
	def freeSpace(self):
		pass
	def generateAndAddPackages(self, links, dest):
		pass
	def generatePackages(self, links):
		pass
	def getAccountTypes(self):
		pass
	def getAccounts(self, refresh):
		pass
	def getAllInfo(self):
		pass
	def getAllUserData(self):
		pass
	def getCaptchaTask(self, exclusive):
		pass
	def getCaptchaTaskStatus(self, tid):
		pass
	def getCollector(self):
		pass
	def getCollectorData(self):
		pass
	def getConfig(self):
		pass
	def getConfigValue(self, category, option, section):
		pass
	def getEvents(self, uuid):
		pass
	def getFileData(self, fid):
		pass
	def getFileOrder(self, pid):
		pass
	def getInfoByPlugin(self, plugin):
		pass
	def getLog(self, offset):
		pass
	def getPackageData(self, pid):
		pass
	def getPackageInfo(self, pid):
		pass
	def getPackageOrder(self, destination):
		pass
	def getPluginConfig(self):
		pass
	def getQueue(self):
		pass
	def getQueueData(self):
		pass
	def getServerVersion(self):
		pass
	def getServices(self):
		pass
	def getUserData(self, username, password):
		pass
	def hasService(self, plugin, func):
		pass
	def isCaptchaWaiting(self):
		pass
	def isTimeDownload(self):
		pass
	def isTimeReconnect(self):
		pass
	def kill(self):
		pass
	def login(self, username, password):
		pass
	def moveFiles(self, fids, pid):
		pass
	def movePackage(self, destination, pid):
		pass
	def orderFile(self, fid, position):
		pass
	def orderPackage(self, pid, position):
		pass
	def parseURLs(self, html, url):
		pass
	def pauseServer(self):
		pass
	def pollResults(self, rid):
		pass
	def pullFromQueue(self, pid):
		pass
	def pushToQueue(self, pid):
		pass
	def recheckPackage(self, pid):
		pass
	def removeAccount(self, plugin, account):
		pass
	def restart(self):
		pass
	def restartFailed(self):
		pass
	def restartFile(self, fid):
		pass
	def restartPackage(self, pid):
		pass
	def setCaptchaResult(self, tid, result):
		pass
	def setConfigValue(self, category, option, value, section):
		pass
	def setPackageData(self, pid, data):
		pass
	def setPackageName(self, pid, name):
		pass
	def statusDownloads(self):
		pass
	def statusServer(self):
		pass
	def stopAllDownloads(self):
		pass
	def stopDownloads(self, fids):
		pass
	def togglePause(self):
		pass
	def toggleReconnect(self):
		pass
	def unpauseServer(self):
		pass
	def updateAccount(self, plugin, account, password, options):
		pass
	def uploadContainer(self, filename, data):
		pass

