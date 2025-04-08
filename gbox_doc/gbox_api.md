# GBox API

  - [gbox](#gbox)
    - [Language](#Language)
      - [namespace](#namespace)
        - [:fixcal](#:fixcal)
        - [:math](#:math)
        - [:task](#:task)		basecall
        - [ease](#ease)
        - [file](#file)		文件系统
        - [font](#font)
        - [keyboard](#keyboard)
        - [sys](#sys)
        - [syshelp](#syshelp)
        - [touch](#touch)
      - [ptrex](#ptrex)
        - [file::ptr](#file::ptr)		系统文件
        - [rsa](#rsa)
          - [rsa::privateKey](#rsa::privateKey)
          - [rsa::publickey](#rsa::publickey)
        - [strtree](#strtree)
      - [res](#res)
        - [GResManager](#GResManager)
        - [res](#res)
        - [resdatptr](#resdatptr)
      - [snd](#snd)
        - [GObjSndStream](#GObjSndStream)
        - [GObjSndView](#GObjSndView)
        - [GWaveFFTShow](#GWaveFFTShow)
        - [snd](#snd)
        - [sndbuf](#sndbuf)
      - [varspace](#varspace)
        - [all kind](#all kind)
        - [bin](#bin)
        - [mat3](#mat3)
        - [mat4](#mat4)
        - [ptr64](#ptr64)
        - [ptrex](#ptrex)
        - [script](#script)
        - [string](#string)		string
        - [var](#var)
        - [vec2](#vec2)
        - [vec3](#vec3)
        - [vec4](#vec4)
    - [obj](#obj)
      - [2dshow](#2dshow)
        - [GObj2DWnd](#GObj2DWnd)
        - [GObjAni](#GObjAni)		2D动画
        - [GObjCamera](#GObjCamera)
        - [GObjDoc](#GObjDoc)		文档显示
        - [GObjEdit](#GObjEdit)
        - [GObjShape](#GObjShape)		常用的2D形状
        - [GObjShow](#GObjShow)		2D显示对象
        - [GObjText](#GObjText)
        - [GObjView](#GObjView)
        - [ext](#ext)
          - [GObjLook](#GObjLook)
          - [GObjSheet](#GObjSheet)
          - [GObjSheetItem](#GObjSheetItem)
          - [GObjSyntaxEdit](#GObjSyntaxEdit)		@mem=多行文本编辑
          - [GObjTxt](#GObjTxt)		多行文本输出,@path=OBJ/2d/ext
        - [help](#help)
          - [ani2d](#ani2d)
          - [con2d::std](#con2d::std)
          - [con2d::tab](#con2d::tab)
          - [con2d:base](#con2d:base)
          - [draw::cmdsz](#draw::cmdsz)
          - [font::text](#font::text)
          - [img](#img)
          - [showcmd](#showcmd)
          - [showpath](#showpath)
      - [3dshow](#3dshow)
        - [GObj3DAni](#GObj3DAni)
        - [GObj3DAniMove](#GObj3DAniMove)
        - [GObj3DBlkMaker](#GObj3DBlkMaker)
        - [GObj3DCharacter](#GObj3DCharacter)
        - [GObj3DHit](#GObj3DHit)
        - [GObj3DLight](#GObj3DLight)		环境灯光
        - [GObj3DLine](#GObj3DLine)
        - [GObj3DShape](#GObj3DShape)
        - [GObj3DShow](#GObj3DShow)
        - [GObj3DSkyBox](#GObj3DSkyBox)
        - [GObj3DWater](#GObj3DWater)
        - [GObj3DWorld](#GObj3DWorld)
        - [atom](#atom)
          - [GObj3DParticle](#GObj3DParticle)
          - [base](#base)
            - [.atombase](#.atombase)		粒子基类,纯基类
            - [atom::ActRibbon](#atom::ActRibbon)		动作条带,基本粒子
            - [atom::Atom](#atom::Atom)		粒子,基本粒子
            - [atom::Ribbon](#atom::Ribbon)		粒子条带,基本粒子
            - [atom::Snow](#atom::Snow)		粒子雪花
          - [ctrl](#ctrl)
            - [.atomctrl](#.atomctrl)		粒子控制基类,纯基类
            - [atom::EBox](#atom::EBox)		盒形发生器
            - [atom::ECircle](#atom::ECircle)		圆形发生器
            - [atom::ELine](#atom::ELine)		线形发生器
            - [atom::ESphere](#atom::ESphere)		球形发生器
            - [atom::Emitter](#atom::Emitter)		点发生器
            - [atom::Fire](#atom::Fire)		目标飞行,粒子控制器
            - [atom::GWell](#atom::GWell)		引力点
            - [atom::Gravity](#atom::Gravity)		重力,粒子控制器
            - [atom::Jet](#atom::Jet)		加速,粒子控制器
            - [atom::R_BindObj](#atom::R_BindObj)		条带控制器
            - [atom::R_Twist](#atom::R_Twist)		条带缠绕控制器
            - [atom::Roto](#atom::Roto)		旋转,粒子控制器
            - [atom::Snd](#atom::Snd)		声音,控制器
            - [atom::Track](#atom::Track)		追踪
            - [atom::Vortex](#atom::Vortex)		漩涡
          - [particle](#particle)		粒子定义
        - [ext](#ext)
          - [GObj3DCamera](#GObj3DCamera)
          - [GObj3DDepMap](#GObj3DDepMap)
          - [GObj3DGuid](#GObj3DGuid)
          - [GObj3DShadowSSM](#GObj3DShadowSSM)
          - [GObjMeshLod](#GObjMeshLod)
        - [help](#help)
          - [ani3d](#ani3d)
          - [material](#material)
        - [mc](#mc)
          - [GMcTreeMaker](#GMcTreeMaker)
          - [GMcWorldObj](#GMcWorldObj)
          - [GObj3DPixelMc](#GObj3DPixelMc)
      - [GObj](#GObj)		基础类
      - [GObjUndo](#GObjUndo)
      - [GWebLink](#GWebLink)
      - [file](#file)
        - [GMIDFileObj](#GMIDFileObj)
        - [GObjLZ4File](#GObjLZ4File)
        - [GObjVDisk](#GObjVDisk)
        - [GObjZipFile](#GObjZipFile)
      - [net](#net)
        - [GNetFileObj](#GNetFileObj)
        - [GSocket](#GSocket)
        - [GSocketC](#GSocketC)
        - [GSocketS](#GSocketS)
        - [GSocketSBase](#GSocketSBase)
        - [GSocketUdp](#GSocketUdp)
        - [GVNetObj](#GVNetObj)
        - [GWebFile](#GWebFile)
        - [csvr](#csvr)
        - [csvr::addr](#csvr::addr)
        - [netapi](#netapi)		DNS net api
        - [web](#web)
      - [os](#os)
        - [GBoxShowApp](#GBoxShowApp)
        - [GObj2DSandBox](#GObj2DSandBox)
        - [GObj3DSandBox](#GObj3DSandBox)
        - [GObjSandBox](#GObjSandBox)
        - [GSandApp2DWnd](#GSandApp2DWnd)
        - [GSandAppWnd](#GSandAppWnd)
        - [GSandBoxWinApp](#GSandBoxWinApp)
        - [locapi](#locapi)
  - [sysgb](#sysgb)
    - [SysKeyMap](#SysKeyMap)
    - [bootnet](#bootnet)
      - [DNSSvrStyle](#DNSSvrStyle)
      - [SysBoot](#SysBoot)
      - [SysNetFile](#SysNetFile)
      - [dnsFile](#dnsFile)
      - [miniBtn](#miniBtn)
      - [miniCon](#miniCon)
      - [miniOutTxt](#miniOutTxt)
      - [miniProg](#miniProg)
      - [netAPISvr](#netAPISvr)
      - [netDownPathDlg](#netDownPathDlg)
        - [TextTitel](#TextTitel)
          - [$miniOutTxt](#$miniOutTxt)
  - [教程](#教程)
    - [3d](#3d)
      - [start](#start)
    - [ex1](#ex1)

#### :fixcal
**类型**:fixcall
**继承**::fixcal
**函数**:
vec4 Color2Hsi(var c)
string Fomatint64X(var v)
var FormatColor(var inval,int bvec4=0)
string FormatInt16Fix(int d,int fixw=0)
string GetHSMStr(int d)
string GetMsStr(var v)
var GetVarInfo(var v)
vec4 Hsi2Color(vec4 vhsi)
var MixColor(var c1,var c2,float mix)
var RGBA(int r,int g,int b,int alpha=255)
var abs(var v)
float acos(float rad)
float ang2rad(float angle):角度转弧度
float asin(float rad)
float atan2(float dy,float dx)
float atan2ang(float dy,float dx)
var clamp(var InValue,var InMin,var InMax)
float cos(float rad)
float dot(var v1,var v2)
float fmod(float x,float y)
string getsizestr(var v)
string gmtsec_str(int gmt,int bcovloc=1)
var makenamedsz(var v)
var makevid(var v)
var max(var pinAgv)
var min(var pinAgv)
var mix(var v0,var v1,float step)
float rad2ang(float rad):弧度转角度
float sin(float rad)
float sqrt(float q)
var sz(var v)
float tan(float rad)
#### :math
**类型**:eve
**继承**::math
**函数**:
bool GetPtOnPlane(vec4 planev4,vec3 p1,vec3 p2,vec3& cross):取线段到平面的交点
vec4 MakePlane(vec3 planepos,vec3 planedir):取V4表示的平面
vec3 SeekPtOnPlane(vec3 planepos,vec3 planedir,vec3 lorig,vec3 ldir):取射线到平面的交点
int rand(int maxv):取0-maxv之间的随机整数
float randf(float range=1.0f):取0.0f-range之间的随机浮点数
#### :task
**类型**:eve
**继承**::task
**函数**:
var Abort(int my,var perragv=NULL)
var BusyWait()
var CallFunEx(var fun,var pagv)
bool DelInterface(obj p,strid pname)
bool EndWait(strid waitnameid,var agv)
void Err(var v)
obj FindInterface(strid facenameid,int bautofindfather=1)
obj GetCurTaskPtr()
string GetFunErrStr(int err)
var HoldTask()
bool IsTaskPtr(obj p)
void RegInterface(obj p,strid pname)
bool RemoveHoldTask(var ptask)
bool ResumeTask(var ptask,var agv)
var StartTask(strid funid,var pstartagv=NULL,strid endfunid=0)
var Wait(float sec,strid waitnameid=0)
var WaitMs(int ms,strid waitnameid=0)
#### ease
**类型**:namespace
**继承**:ease
**函数**:
bool AddWait(float sec,var pvend=NULL)
bool Ani(strid paramname,int mode,var destv,float sec,var pstart=NULL,var pvend=NULL)
void Begin(strid nameid,float waitsec=0)
float Cal(int mode,float t,float b , float c, float d)
void End(int looptime=0)
string GetModeName(int mode)
int GetModeNum()
bool IsHave(strid nameid)
bool Remove(strid nameid)
#### file
**类型**:namespace
**继承**:file
**函数**:
void CheckNotiRegFile():检查所有文件状态
bool CopyFile(string lpExistingFileName,string lpNewFileName,int bFailIfExists=0):拷贝文件,支持文件在各种pak包或IO中
bool DelFileNoti(string pfilename,obj pcall,var pfun=NULL):删除文件状态回调
bool DeleteFile(string fname):删除文件,支持文件在各种pak包或IO中
string FixPath(string path):合并文件名中的..转义
var GetAccessPathSz():取所有可访问的目录属性
string GetFileExtName(string pfullfilename):取全文件名的后缀
var GetFileInfo(string pfilename):取文件信息,成功返回(flen,date,isinpak,isreadly)
int64 GetFileLen(string fname):取文件字节长度()不存在返回0
var GetFileLenTime(string fname):取文件时间
int GetFileNameID(string fname):取文件名ID,不区分大小写
string GetFileNameNoExt(string pfullfilename):取全文件名的名字
int GetFileTime(string fname):取文件时间
string GetFileTimeGMT(int datetime):取文件GMT时间,20xx-xx-11 8:00:00
string GetIDFileName(strid id):取ID文件名
string GetPublicPath():取Gbox共享数据存储路径
string GetRelativePathName(string path,string pathname,int bpathonly=1):取文件名的相对位置
string GetStartFileName():取启动文件名
string GetSysFilePath():取系统文件路径
string GetTempPath():取临时文件存储路径
bool IfHaveFile(string fname, int date=0, int len=0):是否存在指定文件
bool IsAbsFileName(string path):是否为绝对文件名
bool IsFileTrans(string papiname):是否注册文件
var ListDir(string listpath,int bhavesub=0,string pextstr=NULL,int maxnum=4096,int retmode=0):列目录文件名
var ListDirEx(string listpath,int info=1):列目录
bool LoadFileBin(var& pretbin,string pfilename):取二进制文件到BIN
bool LoadFileBinRange(var& pretbin,string pfilename,var startpos,int len):取二进制文件部分到BIN
bool LoadText(var& pstring,string pfilename):取文本文件到string
bool LoadTextSz(var& psz,string pfilename):取文本文件,按行存放sz
bool LoadVarAsFile(var& pret,string pfilename,int key=0):取var文件
string MakeSysFileName(string pfilename):取系统文件名
bool MoveFile(string pexist,string pnew):移动文件
void NotiFileStatus(string plocname,int st):通知文件状态
bool PreWritePath(string lpszFileName):准备写文件的目录
bool RegFileNoti(string pfilename,obj pcall,var fun):注册文件状态回调
bool RegFileTransApi(obj psvr,string papiname,string pfunname):注册文件访问
bool RemoveDir(string path):删除目录
bool RenameFile(string pexist,string pnewname):文件改名
bool SaveFileBin(var& pwbin,string pfilename,int filetime=0):写BIN到文件
bool SaveFileBinRange(var& pwbin,string pfilename,var startpos):写BIN到文件指定位置
bool SaveText(var string,string pfilename,int utf8=1):写文本文件
bool SaveVarAsFile(var& pwritev,string pfilename,int key=0,int filetime=0):保存var文件
bool SetFileTime(string lpszFileName, int time):设置文件时间
void SlipFileName(string &Path,string &name,string pfullfilename):分割全路径文件名
bool UpdateFile(string fname):更新文件,时间到当前,支持文件在各种pak包或IO中
#### font
**类型**:namespace
**继承**:font:task
**函数**:
void ClearAllCache()
bool RegFixImgFont(string pfontname,string pimgname,int w,int h,string pimgnamehi,string poutmaplib=NULL)
bool RegFreeTypeFont(string pfontname,string pfilename,string poutmaplib=NULL)
#### keyboard
**类型**:namespace
**继承**:keyboard:task
**函数**:
void AddKeyChar(string pstr,int bmark=0)
bool IsPress(int key)
bool IsReg()
void Reg(obj p,int keymode=0)
void RegHook(obj pobj,int breg=1)
void SetKeyDown(int key)
void SetKeyUp(int key)
void UnReg(obj p)
#### sys
**类型**:namespace
**继承**:sys:task
**函数**:
bool CopyToClipboard(string cpystring):写剪裁板文本
string GetAppBundleID()
string GetAppPathName()
bool GetClipText(string& clpstr)
var GetDeviceMetrics()
vec2 GetDeviceSize()
string GetIDString(int id)
string GetMac(string pgamename,int needaddins=0)
int64 GetMacID(string pgamename,int needaddins=0)
int GetMacNum()
int64 GetMsCount()
int64 GetOnlyInt64(int hbyte=0)
int GetSecCount()
string GetSelfIPAddress()
var GetStringID(string str)
var GetSystem(strid nameid,var pdef=NULL)
var GetSystemVID()
int GetTickCount()
bool IsClipText()
bool IsSystem(strid nameid)
int LaunchAppliction(string pfilename,string pagv)
bool OpenURL(string purl):打开网页
string ReadPublicString(string strSection,string keyname,string defaultstr=NULL)
var ReadPublicVar(string strSection,string keyname,var pdefault=NULL)
void SetSystem(strid nameid,var v)
bool ShellBrowse(string path)
bool ShellOpenDoc(string pfilename)
bool WritePublicString(string strSection,string keyname,string string)
bool WritePublicVar(string strSection,string keyname,var wv)
#### syshelp
**类型**:namespace
**继承**:syshelp:task
**函数**:
var DefStruct(string structname,var colsz,int isclass=1)
var FindClassCfgVal(var path,var def)
var FindClassPtr(var classname,var pfindclass=NULL):用查找类指针,包括脚本和C++
var GetCfg(string path,var def)
var GetCfgSz(string path,strid musthaveid=0,int getlvl=-1)
int GetClassInfo(var& ret,var pclass,string pfinddef):取类指针中定的信息,"funsz,memsz;[havebase=1],[perstr=a]"
var GetFunInfo(var pfun,strid keyid=0,var pcmpval=NULL)
var GetMarcoDef(int mode=0,var pagv=NULL)
bool GetScriptClassInfo(var& ret,var pobj)
var GetScriptIDStr(strid kindname)
void GetSysAllClassDef(var& all)
void GetSysAllClassPathDef(var& all)
void GetSysIDName(var& all)
bool SetCfg(string path,var v,int bnoti=1)
#### touch
**类型**:namespace
**继承**:touch:task
**函数**:
void Cancel(int id,obj pdel)
void CancelOther(int id,obj pthis)
void ChgObj(int id,obj pthis,obj pto)
void ClearAll()
vec2 GetLastPos()
int GetLinkObjNum(int id)
bool RegHook(obj pobj,int breg=1)
bool RegHookKind(strid hookid,var objorclass,strid hookfunid=0)
void SetTouchHookObj(obj pobj)
bool SetUserAgv(int id,var v)
#### file::ptr
**类型**:ptrex
**继承**:ptrex/file::ptr
**函数**:
void Close():关闭文件
int64 GetFileSize():文件大小
int GetFileTime():取文件时间
bool IsOk():是否打开
bool Open(string pname,int mode=0):打开文件,mode 0:只读,1:写,2:读写
bool SeekRead(var pos,var& bin,int maxlen=0):读数据
bool SeekWrite(var pos,var bin):写数据
bool SetFileSize(var len)
bool SetFileTime(int time):设文件时间
##### rsa::privateKey
**类型**:ptrex
**继承**:ptrex/rsa::publickey/rsa::privateKey
**函数**:
void CreateKey():生成m, e, p, q; 安全级别是1024位
bool EncryptVar(var sv,var& dv)
var GetPrivateKey()
bool SetPrivateKey(var keyv)
##### rsa::publickey
**类型**:ptrex
**继承**:ptrex/rsa::publickey
**函数**:
bool DecryptVar(var sv,var& dv)
var GetPublicKey()
bool SetPublicKey(var keyv)
#### strtree
**类型**:ptrex
**继承**:ptrex/strtree
**变量**:
int datkind
int flag
int isval
int level
int mask
string name
string path
var pidnode
obj pobj
int ref
string sortkey
int subnum
var val
**函数**:
bool Del(string path)
void DeleteSub(int lvl=0,int datmask=0,int submask=0)
var Get(string path,var defv)
int GetDatKind(string path,int datkind=0)
var GetNode(string path)
void GetSubNodeSz(var& ret,int lvl=0,int datmask=0,int submask=0,int sortkind=-1)
void GetSubObjSz(var& ret,int lvl=0,int datmask=0,int submask=0,int sortkind=-1)
var Set(string path,var v,int datkind=0):ret node ptrex
void SetCallBack(obj pc,strid crfunid,strid delfunid=0,strid chgfunid=0)
bool SetMask(int inmask,int bset=1)
void SetSplit(string pcharsz)
void Trace()
#### GResManager
**类型**:class
**继承**:GObj/GResManager
**变量**:
obj m_pStatusNoti
string m_sFilePath
var m_vDatInfo
**函数**:
var GetResData(var resname)
int GetResFileName(var resname,string &locname,var& linksz)
bool IsRes(var resdat)
int LoadRes(string path,string resfilename)
int PerRes(var resname,var& dat)
void RegResCtrl()
void SaveData()
bool SetResData(var resdat)
void SetSvrLink(var psvrlink)
#### res
**类型**:namespace
**继承**:res
**函数**:
int AddResSz(var& sz,var resname)
obj GetCtrl()
int64 GetID(var resname)
var GetImgInfo(var img)
string GetName(var i64,int mode=0)
var GetResData(var resid)
int GetResFile(var resname,string &locname,strid fid=0)
var GetScriptRes()
int64 NewID(int type=0)
bool Start(string pdbname)
#### resdatptr
**类型**:ptrex
**继承**:ptrex/resdatptr
**函数**:
var GetName()
#### GObjSndStream
**类型**:class
**继承**:GObj/GObjSndStream
**变量**:
int m_nBytePerSample
int m_nClns
int m_nFrameSize
int m_nSamplesPerSec
**函数**:
bool CloseOutStream()
bool CloseRecStream()
bool OpenOutStream()
bool OpenRecStream(int recmode=0)
void OutData(var bindata):波形数据
bool SetUdpSender(obj pudp,int ip,int port)
#### GObjSndView
**类型**:class
**继承**:GObj/GObjShow/GObjView/GObjSndView
**变量**:
float m_fVScale
float m_fVal
int m_nShowSampleScale
int m_nSndLenMs
string m_sInfo
**函数**:
void AddData(var bindata)
void AutoScale()
bool CreateData(int hz=8000,int bitpersmaple=2,int chls=1)
bool LoadFile(string pname)
void PlaySel()
void PlaySnd()
bool SaveFile(string pname,int mode=0)
void SelectInViewPos(int sx,int endx)
void SetVal(float n)
#### GWaveFFTShow
**类型**:class
**继承**:GObj/GObjShow/GWaveFFTShow
**函数**:
void Init(int SampleSize=512,int bound=48)
void OnWavData(var bindata):波形数据
#### snd
**类型**:namespace
**继承**:snd:task
**函数**:
bool Play(var sndid,int val=100,int pan=0,int bglfocus=0,int loop=0)
bool Stop(var sndid)
#### sndbuf
**类型**:ptrex
**继承**:ptrex/resdatptr/sndbuf
**函数**:
bool IfPlaying()
bool Load(string fname)
bool Play(int val,int pan,int bloop=0)
bool Save(string fname,int mode=0)
bool SetValume(float val)
bool Stop()
#### all kind
**类型**:varkind
**继承**:var:void
**变量**:
int isnil
int size
**函数**:
int CopyStruct(var pfv):拷贝结构
bool CovStruct(GBR_Task *pTask,var structnameid):转化为结构
bool CreateSpaceStr(string pstr,string psplitstr,string pletchar,var pdef=NULL,int forcestrkind=0)
bool Destroy()
string FormatFloat(int shows=3,int fixspace=0)
string FormatInt(int fixspace=0,int add0=0)
string FormatInt16(int fixspace=0)
string GetSafeStr()
int GetStructCol(strid colname):取结构名数组号
var GetStructDef():取结构定义
string GetStructName():取结构名
var GetStructPtr():取结构ptr64
string GetTrace(GBR_Task *pTask,int mode=0):取调试信息
int GetType()
string GetTypeName()
float GetVec(int no)
int GetVecSize()
bool IsBin()
bool IsEmpty()
bool IsFloat():是否为浮点数
bool IsInt():是否为整数
bool IsInt64():是否为int64
bool IsNum():是否为数字
bool IsPtr():是否为ptr
bool IsPtr64(strid kindid=0)
bool IsPtrEx(strid classid=0)
bool IsScript()
bool IsString()
bool IsStruct(GBR_Task *pTask,var structnameid):是否为结构
bool IsSz():是否为数组
bool IsVec()
bool IsVec2()
bool IsVec3()
bool IsVec4()
bool SetVec(int no,float f)
bool SzAdd(var v)
int SzAddNoSame(var psz)
int SzCovStruct(GBR_Task *pTask,var structnameid,int startpos=0,int step=1)
bool SzDel(int delpos,int len=1)
int SzFind(var psz,int startpos=0,int step=1)
bool SzGet(var& getv,var pos)
int SzHalfSearch(var psz,int breverse=0)
bool SzInit(int size,var pinit=NULL)
bool SzInsert(int insertpos,var v)
int SzIsStruct(GBR_Task *pTask,var structnameid,int startpos=0,int step=1)
void SzLink(var linksz):连接两个sz
bool SzMake(int bszcacel=1)
int SzPtrCallBack(var vfun,var pagv=NULL,int subsize=1,int ptrpos=0):对ptrsz中所有对象调用
int SzPtrFind(obj fptr,int subsize=1,int ptrpos=0):查找对象在ptrsz中位置
int SzPtrPack(int subsize=1,int ptrpos=0):去除sz所有非有效对象数据
int SzSearch(var psz,int startpos=0,int step=1,int subszno=0)
bool SzSort(int order=0,int subszstart=-1)
void Trace(GBR_Task *pTask,color c=0):输出调试信息
var col(strid nameid,var pdef=NULL):取结构列值
bool ifcols(string pcolnamedefs):检查列条件,struct or vid 'colname1>0;colname2;colname3!=nil;...'
bool isobj()
bool vdel(strid nameid):del vid id值
bool vdel64(var id64)
var vget(strid nameid,var pdef=NULL):取vid id值
var vget64(var id64,var pdef=NULL)
var vid(strid nameid,var pdef=NULL):ret vid id ptr
var vid64(var id64,var pdef=NULL):ret vid64 id ptr
bool vidAddSpaceStr(string pstr,string psplitstr,string pletchar,var pdef=NULL,int forcestrkind=0)
bool vis(strid nameid):是否有vid id值
bool vis64(var id64):是否有vid64 id值
bool vset(strid nameid,var v):设vid id值
bool vset64(var id64,var v)
bool vsetsz(var v)
#### bin
**类型**:varkind
**继承**:var:bin
**变量**:
int binsize
int datname
**函数**:
void AddFloat(float f)
void AddInt(int d)
void AddInt64(var i64)
bool Compress_LZ4(var& pret,int flag,int ziplevel=6)
bool DelByte(int pos,int delnum)
void Empty():清空
bool FillByte(int pos,int set,int size)
int FindInt(int d,int st=0,int emsize=4)
bool GetAsStr(var& retstr)
string GetBase64()
int GetBinSize()
int GetByte(int pos)
float GetFloat(int pos)
int GetInt(int pos)
int64 GetInt64(int pos)
int Length()
bool SetAsStr(var str)
bool SetBase64(var str)
void SetBinSize(int size,int addbuf=16)
bool SetByte(int pos,int byte)
bool SetFloat(int pos,float d)
bool SetInt(int pos,int d)
bool SetInt64(int pos,var i64)
bool UnCompress_LZ4(var& pret,int flag)
#### mat3
**类型**:varkind
**继承**:var:mat3
**函数**:
float GetSub(int pos)
void Init():清空
void Init2DMatrix(float scale,float rad,float offx,float offy)
var Inverse():求逆
bool SetSub(int pos,float v)
var Transpose():转置
#### mat4
**类型**:varkind
**继承**:var:mat4
**函数**:
vec3 GetOffSet()
float GetSub(int pos)
void GetTransRotScale(vec3& trans,vec4& rot,vec3& scale)
void Init():清空
void Init2DMatrix(float scale,float rad,float offx,float offy)
void InitRotationX(float rad)
void InitRotationY(float rad)
void InitRotationZ(float rad)
void InitRotationZX(float radz,float radx)
void InitVectorRotation(float x, float y, float z, float a)
var Inverse():求逆
void OffSet(float x,float y,float z)
void Scale(float s)
bool SetSub(int pos,float v)
void SetTransRotScale(vec3 trans,vec4 rot,vec3 scale)
var Transpose():转置
#### ptr64
**类型**:varkind
**继承**:var:ptr64
**函数**:
obj GetObj()
bool IsSysObj()
bool SetObj(obj p)
void Trace()
bool isobj()
#### ptrex
**类型**:varkind
**继承**:var:ptrex
**变量**:
int classid
**函数**:
bool Delete(GBR_Task *ptask)
string GetClassName()
bool GetParam(strid nameid,var& val)
bool IsEmpty()
bool New(GBR_Task *ptask)
bool SetParam(GBR_Task *ptask,strid nameid,var val)
#### script
**类型**:varkind
**继承**:var:script
**函数**:
var CompileExp(GBR_Task *ptask,string pext,var& pvarnamevid)
var SetRuner(obj p)
void Trace(GBR_Task *ptask)
var runExp(GBR_Task *ptask,var& pvarnamevid)
#### string
**类型**:varkind
**继承**:var:string
**变量**:
int length
int size
int strid
int64 strid64
**函数**:
bool Compare(string pstr)
bool CompareMax(string pstr)
bool CompareNoCase(string pstr)
bool CompareNoCaseMax(string pstr)
string CovToNormalStr(int btry=0)
string CovToTextedStr(int bdq=1)
bool CreateWithSafeStr(var& agv)
string DecodeBase64()
void Delete(int pos,int delnum=1)
string EncodeBase64()
int Find(string sfind,int fromindex=0)
int FindEnd(string pfind,int formindex=0):寻找字符串中指定字符串的结束位置
int FindEx(string sfind,int flag,int fromindex=0):flag bitmask 1=case;2=word
int FindInverse(string sfind,int fromindex=0)
int GetAscll(int num):取中间第num个字符的Ascll码
var GetColor(int def,string psplitchar)
var GetFinder(int flag=0):准备字符串查找
float GetFloat(float def,string psplitchar):取字符串浮点数
int GetInt(int def,string psplitchar):取字符串第一整数
int64 GetInt64(int def,string psplitchar):取字符串第一int64整数
bool GetKeyWord(string& retstr):取字符串一个单词
bool GetLastWord(string& retstr,string psplitchar,int bmusthavech=0):取字符串最后一个词
int GetLength()
int GetMidStr(string &retstr,string pfind,string pend,int formindex=0,int bhaveflag=0):寻找字符串中指定字符串之间的字符串，返回的结束位置
bool GetTextSkipStr(string &sret,string psplitchar)
bool GetWord(string& retstr,string psplitchar,int bmusthavech=0,int bmoveempty=1):取字符串第一个词
void Insert(int insertpos,string pstr)
var JsonToStrVal():按Json格式转换为namedvar
string Left(int num)
void MakeLower()
void MakeUpperCase()
void MakeWord():字符串去不可见字符
string Mid(int first, int count)
int OnFind(var finder,int fromindex=0):字符串查找
var PerReplaceSz(var repstrsz)
bool RemoveLastChar(string psplitchar)
int Replace(string pstr,string tostr,int start=0,int maxreplace=0)
int ReplaceSz(var repstrbin,int start=0)
string Right(int num)
void SetLastChar(string psplitchar)
var Split(string psplitstr,int bskipformat=0)
int Str2UINT()
string UrlDecode()
string UrlEncode()
#### var
**类型**:varkind
**继承**:var:var
**变量**:
int size
**函数**:
bool svAdd(string name,var pinit=NULL):增加命名值
bool svDel(string name)
bool svGet(string name,var& pret):取命名值
bool svGetJsonText(string &txt,int bcr=0)
int svPos(string name)
bool svSet(string name,var pinit=NULL):增加替换命名值
var svVal(string name,var pdef=NULL)
#### vec2
**类型**:varkind
**继承**:var:vec2
**变量**:
float x
vec2 xy
float y
vec2 yx
**函数**:
vec3 GetVec3(float z=0)
bool IsZero()
float Length()
void Normalize()
vec2 Roto(float degree)
void Set(float x,float y)
#### vec3
**类型**:varkind
**继承**:var:vec3
**变量**:
float x
vec2 xy
vec3 xyz
float y
vec2 yx
float z
**函数**:
void GetAsEulerMatrix3(var& vmat3)
void GetAsEulerMatrix4(var& vmat4)
vec2 GetVec2()
bool IsZero()
float Length()
void Normalize()
vec3 RotoX(float degree)
vec3 RotoY(float degree)
vec3 RotoZ(float degree)
void Set(float x,float y,float z)
#### vec4
**类型**:varkind
**继承**:var:vec4
**变量**:
float bottom
float left
vec2 lefttop
float recth
float rectw
float right
vec2 rightbottom
float top
float w
float x
vec2 xy
vec3 xyz
float y
float z
**函数**:
void Blend(float d,vec4 q)
int GetColorARGB()
void GetMatrix4(var& pmat)
vec4 InitRotationX(float degree)
vec4 InitRotationY(float degree)
vec4 InitRotationZ(float degree)
vec4 InitRotationZXY(float degz,float degx,float degy)
void InitRotoZTo(vec3 dir,float roll)
void InitShortestArc(vec3 from, vec3 to)
bool IsPtInRect(vec2 pt)
bool IsZero()
void Normalize()
bool RectIsEmpty()
void RectOffset(vec2 off)
vec2 RectSize()
void RectUnion(vec4 s)
void RectUnionPt(vec2 s)
void Roto(vec4 r)
void Set(float x,float y,float z,float w)
void SetColorARGB(int c)
#### GObj2DWnd
**类型**:class
**继承**:GObj/GObjShow/GObj2DWnd
**变量**:
int m_nTopMost:是否为TopMost
vec4 m_vOutRect
var m_vShapeEx
**函数**:
void CloseWnd()
bool CreateOsWnd(int style=0)
void DragAcceptFiles(int bacc=1):设置是否接受外部文件拖放
void Enable(int bable=1)
var FindScrPtWnd(vec2 pt)
void FlashWindow(int bInvert=1):设置是否窗口闪烁
string GetText()
bool IsActive():是否窗口活跃
int IsEnable()
bool IsScrWnd()
void OnDropFiles(vec2 pt,var filenamesz)
void OnWndClose()
void Set2DRender(int b2d=1)
void SetAutoAct(int act)
bool SetOsWinStyle(int style):设置窗口显示风格
void SetText(string pstr):设置窗口标题
void SetTopMost(int btop):设置是否为TopMost
bool SetWinIcon(string piconfilename):设置窗口图标
int SetWndShow(int mode)
#### GObjAni
**类型**:class
**继承**:GObj/GObjShow/GObjAni
**变量**:
float m_fAniSpeed
float m_fAniStartSec
float m_fDegree:整体旋转角度
float m_fFrame
float m_fScale:整体比例
color m_nLineColor
int m_nPlayStatus
int m_nShowLineTrack
ptrex m_pAni
vec4 m_vLineColor:线颜色
**函数**:
void CreateAni()
var GetAniKindSz()
float GetAniLength(strid kindname=0)
bool LoadAni(var name)
void PlayAni(strid kind=0,float start=0,float speed=1)
bool SetAniKind(strid kindname)
void SetDegree(float deg)
void SetFrame(float t)
void SetImgSz(var var)
void SetNoti(int bnoti)
void SetPlayStatus(int mode=1)
void SetScale(float f)
#### GObjCamera
**类型**:class
**继承**:GObj/GObjShow/GObjCamera
**变量**:
float m_fFov
float m_fLookDis
float m_fRoll
float m_fRotoY
float m_fRotoZ
float m_fZf
float m_fZn
int m_nClearBk
color m_nLineColor
int m_nLookMode
obj m_p3DTouchRoot
obj m_pDepObj
obj m_pLookAtObj
obj m_pShadowObj
obj m_pWorld
var m_vCamera
vec3 m_vEyePt
vec3 m_vLookDir
vec3 m_vLookPt
vec3 m_vLowVec
vec3 m_vOffset
vec3 m_vUpVec
**函数**:
bool GetImg(var& imgdata,int w,int h,int scale=1,int bdcolor=0,int bdsize=0)
bool GetPickDir(float x,float y,vec3& org,vec3& dir)
bool GetPickLine(float x,float y,vec3& org,vec3& end)
bool GetPickPtOnPlane(float x,float y,vec3& pt,vec3 planepos,vec3 plandir)
vec3 GetScreenPos(vec3 ptwd)
void OnTouch(var& dn)
void OnTouchWheel(float dz,vec3 pt,int ctrlkey,var extvar)
void SetLookAt(vec3 pt)
bool SetLookAtObj(obj p)
void SetRangeZ(float znear,float zfar)
bool SetWorld(obj pwd)
void UpdateFrustum()
#### GObjDoc
**类型**:class
**继承**:GObj/GObjShow/GObjView/GObjDoc
**变量**:
vec4 m_CursorRc
int m_bAutoFit
int m_bAutoWarp
int m_nActive
int m_nClassNum
color m_nColorEx
int m_nCurX
int m_nCurY
color m_nCursorColor
int m_nFontStyleNum
color m_nHiCurBkColor
int m_nLineNum
int m_nMaxH
int m_nMaxW
int m_nMinH
int m_nMinW
color m_nSelBkColor
int m_nSelMode
color m_nSelTextColor
int m_nSelX0
int m_nSelX1
int m_nSelY0
int m_nSelY1
int m_nStyleNum
int m_nTabNum
color m_nTextColor
string m_sText
var m_vImgMap
vec4 m_vOutRect
var m_vStyleMap
**函数**:
bool AddText(string pstr,int selmode=0)
bool DelSelect()
bool DeleteText(int x0,int y0,int x1,int y1,int selmode=0)
var FindStr(int colx,int coly,string pstr,int flag=0,int strmode=1)
int FindWithFinder(int colx,int coly,var finderv,int &rx0,int &rx1)
int GetPtLine(int x,int y,int &colx)
bool GetPtStyle(var& ret,float ptx,float pty,int mode=0)
string GetSelectText(int mode=0)
string GetSubText(int mode,int x0,int y0,int x1,int y1)
string GetText(int mode=0)
bool InsertText(int colx,int coly,string pstr,int selmode=0)
bool Load(string pfilename)
void MoveCurPos(int dcolx,int dcoly,int selmode=0)
void NeedReCal(int mode=1)
void NoSelect()
bool Save(string pfilename,int mode=0)
bool SelectTextAtLine(int colx,int coly,int num)
void SetAutoFitSize(int bfit)
void SetAutoWarp(int warp)
void SetColorEx(color c)
void SetCurChgEmit(strid eveid)
void SetCurPos(int x,int y,int selmode=0)
void SetCurPtPos(int x,int y,int selmode=0)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetImgMap(strid nameid,var imgsrc)
bool SetLineAlign(int coly,int h,int v)
void SetLineDh(int h)
void SetLineStart(int x)
void SetSelect(int selmode,int x0,int y0,int x1,int y1)
bool SetSelectFontStyle(string pstyle)
void SetSizeLimit(int minw,int maxw,int minh,int maxh)
void SetStyleMap(string pname,string pcmdstr)
void SetText(string ptext)
void SetTextColor(color c)
#### GObjEdit
**类型**:class
**继承**:GObj/GObjShow/GObjEdit
**变量**:
float m_fMarginLeft
float m_fMarginRight
float m_fR:圆角
float m_fTextViewX
color m_nActBkColor:act线颜色
color m_nActLineColor
color m_nActTextColor
int m_nActive
color m_nCurColor
int m_nCurX
int m_nFontEx
int m_nFontW
int m_nItalic
color m_nLineColor
int m_nPass
color m_nSelBkColor
int m_nSelEnd
int m_nSelStart
color m_nSelTextColor
color m_nTextColor
int m_nWeight
string m_sFontName
string m_sText
vec4 m_vCurColor
vec4 m_vFillColor
vec4 m_vLineColor:线颜色
vec4 m_vSelBkColor
vec4 m_vSelTextColor
vec4 m_vTextColor
**函数**:
bool Delete(int i,int num=1)
int GetCharIndex(float locx)
float GetCharPos(int i)
int GetLength()
string GetMidStr(int start,int end)
int GetSelNum()
string GetText()const
void Insert(int i,string ptext)
void SetDef(float x,float y,string ptext,color color=0)
void SetFillColor(color c,int a=0)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetLineColor(color c,int a=0)
void SetShape(color fillc,color linec=0,float r=0)
void SetText(string ptext)
#### GObjShape
**类型**:class
**继承**:GObj/GObjShow/GObjShape
**变量**:
float m_fDegree:整体旋转角度
float m_fFade
float m_fR:圆角
float m_fScale:整体比例
int m_nFrame
color m_nLineColor
vec4 m_vLineColor:线颜色
var m_vShapeEx
**函数**:
var GetImgPtr()
void SetDegree(float deg)
void SetImg(var nameorid,int frameno=-1)
void SetLineColor(color c,int a=0)
void SetScale(float f)
void SetShape(color fillc,color linec=0,float r=0,float fade=0)
void SetShapeExImg(var nameorid,int repeat=1)
#### GObjShow
**类型**:class
**继承**:GObj/GObjShow
**变量**:
float m_fAlpha:取对象alpha透明度
float m_fH:取对象高
float m_fPosBottom
float m_fPosLeft
float m_fPosRight
float m_fPosTop
float m_fW:取对象宽
float m_fX:取对象xpos
float m_fY:取对象ypos
float m_fZ:取对象zorder
int m_nAbsMat
int m_nAlphaInherit:继承alpha
int m_nCanTouch:touch查找标志
int m_nClip:视区剪裁
color m_nColor:颜色
int m_nDisSubTouch:禁止子对象Touch
int m_nDisable:禁止Touch
int m_nEnable:允许Touch&key
int m_nLayer
int m_nPageFlag
color m_nSelBoxColor:选择框颜色
int m_nShow:是否可见
int m_nShowMode:显示模式
int m_nTouchHook
ptrex m_pCon
obj m_pShowWnd
vec4 m_vColor:颜色vec4
vec3 m_vPos:浮点精度vec3坐标
vec2 m_vPos2:浮点精度vec2坐标
vec2 m_vPosCenter
vec4 m_vRect
vec2 m_vRectCenter
vec4 m_vRectPos
vec2 m_vRightBottom
vec2 m_vSize
obj pidshow
**函数**:
void AddCanTouch(int touchmode)
void AddSizeNoti(obj p,strid sizefunid=0,int bcallimm=0):注册当对象尺寸改变后回调 OnSizeNoti
void BringZPos(int mode)
void Center()
void ConPlace(int bimm=0)
void DelSizeNoti(obj p,strid sizefunid=0)
void DeleteAllShowSub(int bonlyshow=0,int bonlythisobj=1):删除所有显示对象
void Enable(int bable=1)
var GetAllShowSubObj(int bonlyshow=0,int bonlythisobj=1):取显示对象数组
float GetHeight():取对象高
vec2 GetLoc2Scr(vec3 pt):转换对象内部坐标到屏幕坐标
bool GetPageFlag(int iflag)
var GetPointObjSz(vec3 pt,int findmode,var agvex)
void GetPtIn(vec3& pt)
void GetPtOut(vec3& pt)
var GetRect()
var GetRectObjSz(vec4 rect,int crossmode,int findmode,var agvex)
vec3 GetScr2Loc(vec2 pt):转换对象屏幕坐标到内部坐标
obj GetShowBefore()
obj GetShowHead()
obj GetShowNext()
obj GetShowSub(int no)
obj GetShowTail()
void GetSize(float &w,float &h):取对象宽高
float GetWidth():取对象宽
bool IsDebug(int flag)const
bool IsPointIn(vec3 locpt):loc(x,y,z)点是否在对象内
bool IsScrPtIn(vec2 scrpt)
bool IsScrWnd()
bool MoveFatherTo(obj ptr,int transpos=1):移动到新的2D对象下
void MoveZPosTo(obj p,int after=1)
void NotiOnSizeChged()
void OffSetPos(float dx,float dy,float dz=0):平面坐标移动
vec2 PlaceShowSubObj(float startx,float starty,float dx,float dy,var ex=NULL)
bool RefConClass(obj pshow)
vec3 ScrPathIn(vec2 pt,var showpath)
void SetAlpha(float alpha):设置显示透明度 cfg
void SetCanTouch(int touchmode)
void SetClip(int bclip):设置是否剪裁 cfg
void SetColor(color c,int a=0)
bool SetConClass(strid conclass=1)
void SetDebug(int flag,int bset=1)
void SetDisSubTouch(int bdisable)
void SetLastShow(int blast=1)
void SetLayer(int layer)
void SetOutClip(int bclip)
bool SetPageFlag(int iflag,int bset=1)
bool SetPerShowFun(strid funnameid)
void SetPos(float x,float y,float z=0):设平面坐标($x,$y)cfg
void SetPosR(float x,float y,float r)
void SetPosSize(float x,float y,float w,float h):设坐标宽高($x,$y,w=100,h=100)cfg
void SetRect(float left,float top,float right,float bottom):设对象Rect尺寸 cfg
void SetSelBoxColor(color c)
void SetShow(int bshow=1):设置是否显示
bool SetShowFather(obj ptr,int transpos=0):移动到新的2D对象下
void SetShowMode(int showmode=0):设置显示模式 cfg
void SetSize(float w,float h):设对象宽高 cfg
void SetTouchHook(strid hid)
bool TransPosTo(obj ptr,vec3& pt):转换坐标
#### GObjText
**类型**:class
**继承**:GObj/GObjShow/GObjShape/GObjText
**变量**:
float m_fAutoFixHeightMax
int m_nAlign
color m_nColorEx
int m_nFixRect
int m_nFontEx
int m_nFontW
int m_nHAlign
int m_nItalic
color m_nTextColor
int m_nUndLine
int m_nVAlign
int m_nWeight
string m_sFontName
string m_sText
vec4 m_vColorEx
vec4 m_vOutRect
vec4 m_vTextColor
**函数**:
string GetText()
void SetAlign(int h=0,int v=0)
void SetAutoFixHeightMax(float h)
void SetColorEx(color c,int a=0)
void SetDef(float x,float y,string ptext,color color=0,int fontsize=0)
void SetFixRect(int b)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetText(string ptext)
void SetTextColor(color c,int a=0)
void SetUndLine(int bundline=1)
#### GObjView
**类型**:class
**继承**:GObj/GObjShow/GObjView
**变量**:
vec4 m_ScrollBkColor
float m_fDegree:整体旋转角度
float m_fFade
float m_fR:圆角
float m_fScale:整体比例
float m_fViewH
float m_fViewW
float m_fViewX
float m_fViewY
int m_nElasticDrag
color m_nLineColor
color m_nScrollBkColor
color m_nScrollColor
int m_nScrollH:显示水平滚动条高
int m_nScrollW:显示垂直滚动条宽
vec2 m_vMapSize
vec4 m_vScrollColor
var m_vShapeEx
vec2 m_vViewOrg
**函数**:
void AddViewNoti(obj p,strid funid,int bcallimm=1)
void DelViewNoti(obj p,strid funid=0)
void MakeRectVisable(vec4 v4,float movesec=0)
void OffSetViewPos(float x,float y,float movesec=0)
void SetMapSize(float w,float h)
void SetShape(color fillc,color linec=0,float r=0,float fade=0)
void SetViewMove(vec2 speed)
void SetViewPer(float perx,float pery,float movesec=0)
void SetViewPos(float x,float y,float movesec=0)
void StopViewMove()
##### GObjLook
**类型**:class
**继承**:GObj/GObjShow/GObjShape/GObjLook
**变量**:
int m_nLookFlag
obj m_pLook
vec3 m_vLookOff
**函数**:
bool IsLookFlag(int flag)const
void SetDirectFlag(strid dshowflag)
bool SetLook(obj pobj)
void SetLookFlag(int flag,int bset=1)
##### GObjSheet
**类型**:class
**继承**:GObj/GObjShow/GObjView/GObjSheet
**变量**:
int m_nColNum
int m_nLineNum
**函数**:
void CreateSheet(int w,int h=0,int defw=0,int deflineh=0)
bool DelCol(int col)
bool DelLine(int y,int count=1)
var GetColCreateData(int x)
var GetColDef(int x,int nameid=0,var pdef=NULL)
int GetColNo(int xpos)
string GetColVarName(int x,int y)
int GetColWidth(int col)
int GetColXpos(int col)
bool GetItem(int x,int y,var& data)
obj GetItemObj(int x,int y,int bcreate=0)
var GetItemObjSz(int x1,int y1,int x2,int y2,int bcreate=0)
bool GetItemRect(int x,int y,vec4& rect)
var GetItemVarNameLink(strid varid)
bool GetLineCreateData(int y,var& ret)
bool GetLineData(int y,var& dat,var& editret)
int GetLineHeight(int y)
int GetLineNo(int ypos)
int GetPtColKind(vec2 pt,int &x,int &y,int kind=0)
int GetSheetColor(int index)
bool GetVarNameCol(string pname,int &x,int &y)
void InsertCol(int col,var pcolcreatedat=NULL)
bool InsertLine(int y,int addnum=1)
void ReCalAllPos()
void ResetSheet()
bool SetColAlign(int col,int a)
bool SetColCreateData(int x,var agv)
bool SetColDef(int col,strid nameid,var val)
bool SetColWidth(int x,int w)
void SetDefLineH(int deflineh)
bool SetItem(int x,int y,var data)
bool SetItemStyle(var stylename)
bool SetLineCreateData(int y,var agv)
bool SetLineData(int y,var dat,var editret)
bool SetLineHeight(int y,int h)
bool SetSheetColor(int index,color c)
##### GObjSheetItem
**类型**:class
**继承**:GObj/GObjShow/GObjSheetItem
**变量**:
int m_nAlgin
int m_nX
int m_nY
string m_sText
var m_vData
var m_vEditData
var m_vShapeEx
**函数**:
void DestroyData(int onlyedit=0)
var GetColDef(strid nameid,var pdef=NULL)
bool GetCreateData(var& v,int onlyedit=0)
void GetData(var& data)
int GetItemColor(int index)
void OnTouch(var& dn)
bool SetCreateData(var v,int onlyedit=0)
void SetData(var data)
void SetDataEdit(var data,var editdata)
void SetItemAlgin(int mode)
void SetItemColor(int index,color c)
void SetText(string ptext)
##### GObjSyntaxEdit
**类型**:class
**继承**:GObj/GObjShow/GObjView/GObjSyntaxEdit
**变量**:
int m_CurLineBkColor
int m_SelectBkColor
int m_nBkColor
int m_nCurCol
int m_nCurLineNo
int m_nCursorColor
int m_nCursorX
int m_nCursorY
int m_nHiShowKind
int m_nHiWordColor
int m_nIsModi
int m_nLeftMargin
int m_nLeftMarginColor
int m_nLineNum
int m_nLineNumColor
int m_nReadOnly
string m_sTextCodeMode
**函数**:
void Active()
bool AddLine(string pstr)
bool CopySelectToClipBoard()
bool DeleteSelect()
int GetCharIndexOfTxt(int line,int col)
var GetColorTab()
string GetFileName()
string GetLine(int i)
vec2 GetLineCharPos(int line,int index)
int GetLineExpStatus(int lineno)
int GetLineHeight()
int GetLineHide(int lineno)
int GetLineIcon(int lineno)
var GetLineIconMaskSz(int iconmask)
vec2 GetLinePt(int lineno,int col=0)
int GetLineWidth(int lineno)
bool GetLineWordSz(int lineno,int col,var& wordsz,int &colno)
bool GetPtLineNo(vec3 pt,int& lineno)
bool GetPtLineNoCol(vec3 pt,int& lineno,int &col)
int GetSelectColEnd()
int GetSelectColStart()
int GetSelectLineNum()
string GetSelectText()
bool GetText(string &str)
int GetTextColor(string pstxname=NULL)
string GetWord(int line,int col)
var GetWordDef(int line,int col)
bool GoToLine(int lineno,int x=-1)
bool HideAllLine(int level)
bool IfCurInSelect(int blinecheck=1)
void InsertText(string ptext,int bsel=0)
bool Load(string pfilename)
void LoadEx(string ptrinfo)
void LoadSyntax(string pstxname):加载语法定义文件
void MakeCaretVisable(int outsize=0)
int MakeLineVisable(int lineno,int col=0)
void MoveCursor(int dx,int dy)
bool MoveSelectToCur(int bcopy=0)
void OnKeyChar(string pstr,int bmark)
void OnKeyDown(int key,int keydata)
void OnKeyFocus(int act)
void OnLBDClick(int x,int y,int flag)
void OnLBDown(int x, int y,int flag)
void OnLBUp(int x, int y,int flag)
void OnMouseMove(int x,int y,int flag)
bool Save(string pfilename=NULL)
void SelectAll()
bool SelectText(int x1,int y1,int x2,int y2)
void SetAutoFitSize(int bfit)
void SetColorTab(var v)
void SetCurChgEmit(strid id)
void SetCurPos(int x,int y)
void SetCurSelect(int bclear=1)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetHiWord(string s,int kind=0)
bool SetLine(int i,string pstr)
bool SetLineBkColor(int i,int color)
bool SetLineIcon(int lineno,int icon)
bool SetLineTips(int i,string pstr)
void SetText(string pstr)
void SetTextColor(color c,string pstxname=NULL)
bool TagLineHide(vec3 pt,int mode=0)
bool TagLineIcon(int lineno,int iconmask)
##### GObjTxt
**类型**:class
**继承**:GObj/GObjShow/GObjView/GObjTxt
**变量**:
int m_nAutoButtomView
int m_nBottomSpaceLine
color m_nColorEx
int m_nCurLineNo
color m_nFillColor
color m_nHiBkColor
color m_nHiTextColor
int m_nIconBd
color m_nIconBk
int m_nLineHeight
int m_nLineNum
int m_nMaxLine
vec4 m_vHiBkColor
vec4 m_vHiTextColor
**函数**:
void AddErr(string pline)
int AddLine(string pline,int color=0,int icon=0,var pMsg=NULL)
void AddMsg(string pline)
void ClearAll()
bool DelLine(int lineno,int num=1)
string GetLine(int lineno)
int GetLineColor(int lineno)
int GetLineIcon(int lineno)
var GetLineMsg(int lineno)
vec2 GetLinePt(int lineno)
bool GetPtLineNo(vec3 pt,int& lineno)
bool InsertLine(int lineno,string pline,int color=0)
bool Load(string pfilename)
int MakeLineVisable(int lineno)
void RegAsTrOut(int bdef=1)
bool Save(string pfilename,int mode=0)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetIcon(var nameorid,int w,int h)
bool SetLine(int lineno,string pstr)
bool SetLineColor(int lineno,color color)
bool SetLineIcon(int lineno,int icon)
bool SetLineMsg(int lineno,var v)
##### ani2d
**类型**:ptrex
**继承**:ptrex/resdatptr/ani2d
**变量**:
int m_nTrackNum
string m_sName
var m_vImgSz
**函数**:
int AddFrameKey(int trno,float t,var pdef=NULL)
bool AddKind(string pname)
int AddTrack(string pname,int w,int h,int imgno)
bool ChgCurTrack(int f,int to)
bool DelFrameKey(int trno,int no)
bool DelTrack(int tno)
void Destroy()
var GetCurTrack(int trno,int mode=0)
var GetFrameKey(int trno,int keyno,strid mode)
var GetKindSz()
bool Load(string fname)
bool Save(string fname)
bool SetCurKind(strid kid)
bool SetCurTrack(int trno,var dat)
bool SetFrameKey(int trno,int keyno,var v)
bool SetFrameKeyPt(int trno,int keyno,int ptnum,strid mode,var v)
void SetImgSz(var imgsz)
##### con2d::std
**类型**:ptrex
**继承**:ptrex/con2d:base/con2d::std
**变量**:
int m_nAlignH
int m_nAlignV
int m_nDx
int m_nDy
int m_nMaxH
int m_nMaxW
int m_nMinH
int m_nMinW
string m_sModeName
**函数**:
void SetAlign(int h=0,int v=0)
void SetLimit(int minw,int minh,int maxw,int maxh)
void SetMode(strid modesid,int dx=0,int dy=0)
##### con2d::tab
**类型**:ptrex
**继承**:ptrex/con2d:base/con2d::tab
**变量**:
float m_fDx
**函数**:
void AddCol(float w,var def)
void CreateCol(int num,float defw=50)
bool GetColDef(int no,var& ret)
bool SetColDef(int no,var def)
bool SetColW(int no,float w)
##### con2d:base
**类型**:ptrex
**继承**:ptrex/con2d:base
**变量**:
float m_fBorderBottom
float m_fBorderLeft
float m_fBorderRight
float m_fBorderTop
vec4 m_vBorder
**函数**:
void LinkNeedPlace()
void SetBorder(float left,float top,float right,float bottom)
void SetMoveFun(var v)
##### draw::cmdsz
**类型**:ptrex
**继承**:ptrex/draw::cmdsz
**函数**:
void Bar(float x,float y,float w,float h,color color=0)
void BeginDraw(int reset=1)
void Destroy():virtual enum FUNRET_ENUM OnPtrExCmd(GBOXSTRID cmdid,const GVar *pagv,int agvsznum,void *pdata,int datalen);
void EndDraw()
void Line(float x1,float y1,float x2,float y2,color color=0)
void OffSetRect(float left,float top,float right,float bottom,int bin=0)
void SetAlign(int hv)
void SetClip(float left,float top,float right,float bottom,int binout=0)
void SetColor(color c1,color c2,color c3=0,color c4=0)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetFontWeight(int w)
void SetLineMode(float linew,int linemode=0,float anispeed=0)
void SetPosR(float x,float y,float r)
void SetRect(float left,float top,float right,float bottom)
void Shape(color fillc,color linec=0,float r=0,float fade=0)
void Text(float x,float y,string ptext,color color=0)
##### font::text
**类型**:ptrex
**继承**:ptrex/font::text
**变量**:
float m_fX
float m_fY
float m_fZ
int m_nAlign
color m_nColorEx
int m_nFixRect
int m_nFontEx
int m_nFontW
int m_nItalic
color m_nTextColor
int m_nWeight
string m_sText
vec3 m_vPos
vec2 m_vPos2
**函数**:
void DrawTo(var pimg)
string GetText()
void SetAlign(int h=0,int v=0)
void SetFixRect(int b)
void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)
void SetFontSize(int w,int h=0)
void SetPos(float x,float y,float z=0)
void SetText(string ptext)
void SetTextColor(color c)
##### img
**类型**:ptrex
**继承**:ptrex/resdatptr/img
**变量**:
int height:取图象高度
int imgbyteper:取图象格式每像素字节数
int imgkind:取图象格式
int width:取图象宽度
**函数**:
void Bar(int x1,int y1,int w,int h,color color):画色块
void Bit(var pimg,int x,int y):拷贝图象
void Blur(int x1, int y1, int x2, int y2,int radius=2):模糊
void Clear(color color=0):清除图象
bool Create(int w,int h):创建图象,单位为像素
void FillCircle(int x1,int y1,int x2,int y2,color color):画圆
bool GetImgData(var& pret,strid format,int q=90):取图象bindata,format="jpg"|"png"
int GetPixel(int x,int y):取点颜色
void Line(int x1,int y1,int x2,int y2,color color,int steps=1):画线
bool Load(string fname)
void PutPixel(int x,int y,color color,int alpha=255):画点
bool SavePng(string pname):保存图象
bool SetAlphaImg(var imgres)
bool SetImgData(var data):设图象bindata
##### showcmd
**类型**:namespace
**继承**:showcmd:task
**函数**:
var Make(var cmd)
##### showpath
**类型**:namespace
**继承**:showpath:showhelp
**函数**:
var Make(obj pobj,var pidsz,obj pend)
bool PtIn(var showpath,vec3& pt)
bool PtOut(var showpath,vec3& pt)
#### GObj3DAni
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DAni
**变量**:
int m_bPlay
float m_fAniSpeed
float m_fAniTime
float m_fBaseCircleR
float m_fOutLineWidth:轮廓线大小
int m_nAniID
color m_nBaseCircleColor:选择圆颜色
int m_nOutlineAlways:是否outline穿透
color m_nOutlineColor:轮廓线颜色
ptrex m_p3DAni
vec4 m_vCullSphere
vec4 m_vOutlineColor:轮廓线颜色vec4
**函数**:
void AddAniNoti(obj pobj,strid callfunid)
void AddReadNoti(obj pobj,strid callfunid)
var CreateAni()
int DelPart(strid partname)
bool GetTagMat4(strid tagnameid,var& mat4)
bool IsAniReady()
void LinkTag(strid tagnameid)
bool Load(var name)
void OnAniReady()
void PlayAni(strid aniid,float st=0)
void PlayAniRet(strid aniid,float speed=0,strid endfunid=0)
int ResetPart()
void SetAniKind(strid aniid)
int SetPart(strid partname,var loadid,strid tagnameid=0,int badd=0)
bool SetPartMaterial(strid partname,strid paramid,var val)
void SetPlay(int bplay=1)
#### GObj3DAniMove
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DAni/GObj3DAniMove
**变量**:
int m_bFlying
int m_bOnGround
var m_vActMap
**函数**:
void GetMoveAgv(var& agv):virtual void Prepare3DShow(PREPAREDATA3D_TYPE &perdata,const GMatrix4 &matworld,bool bmatworldchged);
bool GetMovePath(var& ret)
int GetStatus()
string GetStatusName()
void InitBlock(float r,float h,float mt=1.0f)
bool Jump(float speed,int bforce=0)
void LockStatus(int block=1)
bool RandGo(vec3 to,float speed)
bool SetMoveAgv(var agv)
bool SetMovePath(var path,float speed)
void StopWalk()
bool ToIdel()
void WalkAngle(float f,float wspeed,float ry=0.0f)
bool WalkTo(vec3 to,float speed,float fnear=1.0f,int testmax=6500)
#### GObj3DBlkMaker
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DBlkMaker
**变量**:
int m_nShowTrMode
**函数**:
void CreateBuf(int w,int h,int subnum=2)
#### GObj3DCharacter
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DAni/GObj3DCharacter
**变量**:
float m_fManHeight
float m_fManR
float m_fObjRotoZ
float m_fUpH
color m_nShowPathColor
var m_vActMap
**函数**:
bool IsMove()
bool Jump(float speed,float g=-9.8f):跳跃
bool ToIdel()
bool WalkAngle(float angle,float speed)
bool WalkTo(vec3 topos,float speed,float nearr=0)
#### GObj3DHit
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DHit
**函数**:
void AddLink(obj pobj,float r,int flag=0,int mask=0,strid callback=0)
void ClearLink(obj pobj)
void Reset()
#### GObj3DLight
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DLight
**变量**:
float m_fAmbient:设置环境光强度
float m_fLight:设置光源强度
float m_fPointLen:点光源半径
**函数**:
void SetDirectional(float f):设置为平行光
void SetLocPointLight(float r):设置为点光源
#### GObj3DLine
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DLine
**函数**:
void AddBox(vec3 p1,vec3 p2,int color=0)
void AddCoordinate(float s=10,float orgw=0.5)
void AddDefCoordinate(float s=11,float dt=1,float sd=0.2f)
void AddLine(vec3 pos1,int color1,vec3 pos2,int color2)
void AddLineSz(vec3 pos1,int color1,vec3 pos2,int color2,int num,vec3 off)
void AddRect(float w,float h,int color=0)
var AddText(string ptext,vec3 p,color textc=0)
void AddTr(vec3 p1,vec3 p2,vec3 p3,int c)
void DeleteText(int no=-1)
void Reset()
void SetCullBox(vec3 pos1,vec3 pos2)
#### GObj3DShape
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DShape
**函数**:
void Destroy()
void SetBox(float w=1.0f)
void SetBoxEx(vec3 p1,vec3 p2)
void SetFace(float w=1.0f)
void SetRenderLayer(int l)
void SetSphere(float r=1.0f,int level=0)
void SetTexture(var nameorid)
#### GObj3DShow
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow
**变量**:
float m_fForward
float m_fScale
int m_nCollisionID:地形碰撞ID
int m_nColorWrite
int m_nDoubleface:双面
int m_nHitFlag:碰撞检测标志
int m_nNoLight:无光照
int m_nShowCullBall
int m_nShowCullBox
int m_nShowNormalLine
int m_nWireframe:线框模式
int m_nZTest
int m_nZWrite
obj m_pWorld
var m_vMatToWorld
vec4 m_vRoto
vec3 m_vScale
mat4 m_vWorldMatrix
**函数**:
void CanShadow(int bcan):设置能否阴影
vec3 DirLoc2World(vec3 dir):转换局部坐标方向到世界坐标
vec3 DirWorld2Loc(vec3 dir):转换世界坐标方向到局部坐标
bool GetCullBoxMinMax(vec3& min,vec3& max):8
var GetMatToWorld()
int GetWorldStandPos(vec3& v,float upmax=1)
void OnShadow(int bon):设置是否阴影
void OnSnow(int bcan):设置是否接受雪
vec3 PtLoc2World(vec3 point):转换局部坐标点到世界坐标
vec3 PtWorld2Loc(vec3 point):转换世界坐标点到局部坐标
void Roto(vec4 q)
void RotoX(float degree)
void RotoY(float degree)
void RotoZ(float degree)
void SetCollisionID(int id)
void SetForward(float degree)
void SetWireframe(int b)
#### GObj3DSkyBox
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DSkyBox
**变量**:
int m_nHalfText
**函数**:
void SetTexture(var texname,int half=1):设置贴图
#### GObj3DWater
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DWater
**变量**:
float m_fLightChgSpeed
float m_fLookDepth:透视距离
float m_fRefractBias:反射比例
float m_fRefractPower:高光指数
float m_fTextrueScaleX
float m_fTextrueScaleY
float m_fWaveSpeed
float m_fWaveSpeedZ
float m_fZscale:起伏比例
int m_nLinkLookAt:视点关联
int m_nReflectMap:是否反射
**函数**:
float GetHeight()
float GetWidth()
void InitWater(var waterbump1name,var waterbump2name)
void LoadLightImg(int no,var filename)
void SetRefract(float refractBias,float refractPower)
void SetSize(float w,float h)
bool SetTexture(int no,var imgname)
#### GObj3DWorld
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DWorld
**变量**:
float m_fAniSpeed:设置动画播放速度
float m_fSnowLevel
int m_nLightWorld
int m_nShowCollision
**函数**:
var GetCollisionInfo(vec3 p0,vec3 p1,var pmat4=NULL,int mode=0)
var GetCollisionLineCross(vec3 org,vec3 end,int mode=0)
int GetCollisionStandPos(vec3& v,float upmax)
var GetShpereHit(vec3 pos,float r,int hitmask,int crossmode=0)
void RefCollision(float x0,float y0,float x1,float y1)
void SetCollisionTexeure(var nameorid)
void SetSelTexeure(var nameorid)
void SetShowCollision(int mode)
void SetSnowTexeure(var nameorid)
##### GObj3DParticle
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DParticle
**变量**:
float m_fPlaySpeed
ptrex m_pAtom
**函数**:
bool Load(var name)
void Reset()
###### .atombase
**类型**:ptrex
**继承**:ptrex/.atombase
**变量**:
ptrex m_pDef
**函数**:
var AddCtrl(string pclassname)
bool DelCtrl(int no)
var GetCtrlSz()
###### atom::ActRibbon
**类型**:ptrex
**继承**:ptrex/.atombase/atom::ActRibbon
**变量**:
GL_ImgPtr m_Texture:贴图
float m_fAlpha:透明比例,def=1
float m_fEndSteps:结束帧数
float m_fOutSpeed:离心速度
float m_fShowTick:拖尾延时
float m_fStartSteps:开始帧数,从指定帧开始生成
float m_fTick:每帧,0.01到0.9之间越小越密
float m_fUScale:贴图U比例,def=1
int m_nBindObjNo:绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它),def=1
int m_nBlue:蓝色,def=255
int m_nGreen:绿色,def=255
int m_nLoop:循环,类型:枚举(0=单次,1=循环),def=0
int m_nRed:红色,def=255
int m_nShowMode:显示方式,类型:枚举(0=正常,1=2X,2=亮度叠加,3=亮度相减,4=取最大值),def=2
string m_sAniName:动画名
string m_sBTag:绑定Tag名
string m_sName:名字,def=""
vec3 m_vMakeP1:起点
vec3 m_vMakeP2:终点
**函数**:
void Enable(int bable)
void Start():virtual void OnPrepareAtomUpdate(GObj3DParticle *particle,const GMatrix4 &matworld,PREPAREDATA3D_TYPE &perdata,DWORD ct,float usetf);
###### atom::Atom
**类型**:ptrex
**继承**:ptrex/.atombase/atom::Atom
**变量**:
GL_ImgPtr m_Texture:贴图
float m_fAniU:贴图动画U,def=0,UV动画速度 u分量
float m_fAniV:贴图动画V,def=0,UV动画速度 v分量
float m_fBiasSlope:显示Z偏移,def=0
float m_fFrameBegin:模型起始帧,def=0
float m_fFrameEnd:模型结束帧,def=1000
float m_fMass:粒子质量,def=1
float m_fSpeedStretch:速度拉伸,def=0
int m_nAlginOrg:对齐方式,类型:枚举(0=lefttop,1=centertop,2=righttop,3=leftcenter,4=centercenter,5=rightcenter,6=leftbottom,7=centerbottom,8=rightbottom,9=镜像中心),def=4
int m_nBillboardKind:公告板模式,类型:枚举(0=无,1=照相机,2=保持方向),def=1
int m_nBindObjNo:坐标系绑定对象,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它),def=0,
int m_nBindToPos
int m_nShowMode:显示方式,类型:枚举(0=正常,1=世界光照,2=亮度叠加,3=颜色叠加,4=2X),def=0
int m_nVisualQuota:最大粒子数,def=999
int m_nWorldSpace:是否世界坐标,类型:枚举(0=否,1=是 绑定对象失效),def=0,
string m_sBTagName:坐标系Tag名,设置序号:tagname,def=""
string m_sName:名字,def=""
var m_vAtomAlpha:粒子Alpha,类型:GFloatTimerSz,def=1
var m_vAtomBlue:粒子Blue,类型:GFloatTimerSz,def=1
var m_vAtomGreen:粒子Green,类型:GFloatTimerSz,def=1
var m_vAtomRed:粒子Red,类型:GFloatTimerSz,def=1
var m_vAtomScale:粒子大小,类型:GFloatTimerSz,def=1
var m_vBindModel:模型名,类型:res(3dani),def=nil
**函数**:
void Enable(int bable)
void MakeAtom(int life,vec3 pos,vec3 speeddir,float sizew=1.0f,float angle=0,float sizeh=0.0f)
void PlayAt(vec3 pos,float angle=0)
###### atom::Ribbon
**类型**:ptrex
**继承**:ptrex/.atombase/atom::Ribbon
**变量**:
GL_ImgPtr m_Texture:贴图
float m_fAlpha:透明比例,def=1
float m_fSpeedScale:速度透明比例
int m_nBindObjNo:绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它),def=0
int m_nOutTimer:拖尾延时,ms
int m_nShowMode:显示方式,类型:枚举(0=正常,1=世界光照,2=亮度叠加,3=颜色叠加,4=2X),def=2
string m_sBTag:绑定Tag名
string m_sName:名字,def=""
**函数**:
void Start()
###### atom::Snow
**类型**:ptrex
**继承**:ptrex/.atombase/atom::Snow
**变量**:
GL_ImgPtr m_Texture:贴图
float m_fAngle:偏转扰动,方向上的偏转角度
float m_fScale:粒子大小
float m_fSpeedOut:扰动系数,数字越大越明显
int m_nAlpha:粒子Alpha,0-255
int m_nBlue:粒子蓝色,0-255
int m_nBottom:底,米
int m_nGreen:粒子绿色,0-255
int m_nMaxSnow:最大粒子数
int m_nRed:粒子红色,0-255
int m_nShowMode:显示方式,类型:枚举(0=正常,1=世界光照,2=亮度叠加,3=颜色叠加,4=2X),def=0
int m_nSnowW:半长宽,米
int m_nTestCross:碰撞方式,类型:枚举(0=无,1=世界碰撞)
int m_nTop:顶高,米
string m_sName:名字
vec3 m_vDirection:运动方向,设置粒子运动的基本方向
**函数**:
void Start()
void Stop()
###### .atomctrl
**类型**:ptrex
**继承**:ptrex/.atomctrl
**变量**:
ptrex m_pAtom
###### atom::EBox
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Emitter/atom::EBox
**变量**:
float m_fDepht:Box深Z,def=1
float m_fHeight:Box高Y,def=1
float m_fWidth:Box宽X,def=1
###### atom::ECircle
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Emitter/atom::ECircle
**变量**:
float m_fMaxRadius:最大半径,def=1
float m_fMinRadius:最小半径,def=1
float m_fStartStep:起始角度,def=0
float m_fStep:步进角度,def=10
###### atom::ELine
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Emitter/atom::ELine
**变量**:
float m_fMaxDeviation:坐标误差,def=0.05
int m_nEndBindObjNo:终点对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0
string m_sEndTag:终点对象Tag名,设置序号:tagname,def=""
vec3 m_vEndPosition:终点坐标
###### atom::ESphere
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Emitter/atom::ESphere
**变量**:
float m_fMinRadius:球半径,def=3
int m_nIsHalf:是否半球,类型:枚举(0=否,1=是),def=1
###### atom::Emitter
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Emitter
**变量**:
var m_fAngle:粒子偏转,类型:GFloatTimerSz设置发生粒子在方向上的偏转角度,def=40
var m_fParticleLife:生命周期,类型:GFloatTimerSz
var m_fRoll:粒子自旋,类型:GFloatTimerSz设置发生粒子的自旋
float m_fStartHeight:粒子高度,发生粒子的初始高度,def=0
float m_fStartSize:粒子宽度,发生粒子的初始宽度,def=1
var m_fVelocity:初速率,类型:GFloatTimerSz
int m_nBindObjNo:起点对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0
int m_nChanceToEmit:发生几率,单位为百分比,def=100
int m_nDelay:发生间隔,发生粒子持续时间结束后距离下一次发生粒子之间的时间,def=0
int m_nDelayFirst:首次延迟,第一次发生粒子之前延迟,def=0
int m_nDirKind:方向类型,类型:枚举(0=无,1=人物方向,2=人物目标,10=发生绑定),def=0
int m_nEmitDuration:持续时间,发生粒子的持续时间,def=1000
int m_nEmitRate:发生数量,发生间隔内发生粒子数量，单位为个,def=5
int m_nNumLoops:循环次数,-1为无限循环0为只发生一次不循环,def=-1
int m_nRotoKind:偏转类型,类型:枚举(0=无,1=人物方向,2=人物目标),def=0
string m_sBTagName:起点对象Tag名,设置序号:tagname,def=""
vec3 m_vDirection:粒子方向,设置发生粒子的方向,def=v3(0,0,1)
vec3 m_vPosition:发生坐标,设置粒子发生器的坐标,def=v3(0,0,0)
**函数**:
void MakeAt(vec3 pos,float fw)
###### atom::Fire
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Fire
**变量**:
float m_fFlySpeed:飞行速度,飞行速度,def=1
float m_fMakeLen:尾烟间隔,尾烟间隔,def=0.2
float m_fMakeLen2:尾烟2间隔,尾烟2间隔,def=0.2
float m_fParticleLife:尾烟生命
float m_fParticleLife2:尾烟生命2
float m_fSinT:发射角度,发射角度,def=30
int m_nBindObjNo:起点对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0
int m_nDelayFirst:首次延迟,第一次发生粒子之前延迟,def=1
string m_sBindTagName:起点对象Tag名,设置序号:tagname
string m_sDMake:尾烟粒子
string m_sDMake2:尾烟粒子2
string m_sEnterAct:爆炸粒子
vec3 m_vEndOff:终点偏移,粒子发生偏移坐标,def=v3(0,0,1)
vec3 m_vStartOff:起点偏移,粒子发生偏移坐标,def=v3(0,0,1)
###### atom::GWell
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::GWell
**变量**:
float m_fGg:加速比率
float m_fRad:核心半径
var m_fRate:引力加速,类型:GFloatTimerSz
int m_nBindObjNo:绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0
string m_sBindTagName:绑定对象Tag名,设置序号:tagname
string m_sEnterAct:点进入启动粒子
vec3 m_vPosition:中心坐标
###### atom::Gravity
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Gravity
**变量**:
vec3 m_vGravity:重力方向,控制粒子加速方向
###### atom::Jet
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Jet
**变量**:
var m_fAcceleration:加速度,类型:GFloatTimerSz
###### atom::R_BindObj
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::R_BindObj
**变量**:
int m_nBindObjNo:绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它)
int m_nDelayFirst:延迟,第一次发生粒子之前延迟
int m_nDuration:持续时间,发生粒子的持续时间
string m_sBTag:起点Tag名
string m_sETag:终点Tag名
vec3 m_vEOff:终点坐标偏移
vec3 m_vSOff:起点坐标偏移
###### atom::R_Twist
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::R_Twist
**变量**:
float m_fRWidth:条带宽度,发生条带宽度m
float m_fRotoTime:旋转时间,旋转一圈秒数
int m_nBindObjNo:绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它)
int m_nDelayFirst:延迟,第一次发生粒子之前延迟
int m_nDuration:持续时间,发生粒子的持续时间
int m_nRotoMode:缠绕方式,类型:枚举(0=绕X,1=绕Y,2=绕Z)
string m_sBTag:起点Tag名
var m_vOff:条带偏移,类型:GFloatTimerSz
var m_vRad:条带半径,类型:GFloatTimerSz
vec3 m_vSOff:起点坐标偏移
###### atom::Roto
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Roto
**变量**:
var m_fRotationSpeed:旋转速率,类型:GFloatTimerSz
###### atom::Snd
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Snd
**变量**:
int m_nDelay:发生间隔,发生粒子持续时间结束后距离下一次发生粒子之间的时间,def=0
int m_nDelayFirst:首次延迟,第一次发生粒子之前延迟,def=0
int m_nNumLoops:循环次数,-1为无限循环0为只发生一次不循环def=1
int m_nSndVal:音量,def=100
var m_vSndName:音效资源,类型:res(snd),def=nil
###### atom::Track
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Track
**变量**:
float m_fG:加速度
float m_fMaxSpeed:最大速度
float m_fRt:转角速度,0-1 速度大转方向快
int m_nBindObjNo:绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0
string m_sBindTagName:绑定对象Tag名,设置序号:tagname
string m_sEnterAct:点进入启动粒子
vec3 m_vPosition:中心坐标
###### atom::Vortex
**类型**:ptrex
**继承**:ptrex/.atomctrl/atom::Vortex
**变量**:
float m_fAngle:方向偏角
float m_fRate:旋转离心力
vec3 m_vDirection:旋转轴方向
vec3 m_vPosition:中心坐标
##### particle
**类型**:ptrex
**继承**:ptrex/resdatptr/particle
**变量**:
float m_fScale:缩放比例,def=1
float m_fSelecR:选择球半径,def=1
float m_fWdLightR:全局灯光半径,def=0
int m_nPlaySpeed:播放速度,def=1000
int m_nSndVal:音量,def=100
int m_nTotalTime:总时长,豪秒,def=-1
string m_sName:名字,def=""
var m_vSndName:音效资源,类型:res(snd),def=nil
vec3 m_vWdLightColor:全局灯光颜色,def=v3(0,0,0)
vec3 m_vWdLightPos:全局灯光位置,def=v3(0,0,0)
**函数**:
var AddAtom(string pclassname)
bool DelAtom(int no)
var GetAtomSz()
bool Load(string fname)
bool SetAsText(string pstr)
##### GObj3DCamera
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DCamera
**变量**:
var m_vCamera
##### GObj3DDepMap
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DDepMap
**变量**:
int m_nTextLevel
**函数**:
void SetTextLevel(int level)
##### GObj3DGuid
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DGuid
**变量**:
int m_bTitle45
color m_nLineColor
int m_nSubH
int m_nSubW
**函数**:
void Clean()
void Create(int xnum,int ynum,int subw=32,int subh=32)
var GetGuidImg(int x,int y)
vec3 GetGuidPos(int x,int y,int btrans=1)
bool SetGuidImg(int x,int y,int imgno,int f)
void SetImgSz(var var)
bool TestLineCallBack(vec3 start,vec3 end,float linew)
##### GObj3DShadowSSM
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DShadowSSM
**变量**:
float m_fDepthBias
float m_fFov
float m_fLightDis
float m_fMaxDis
float m_fT0
float m_fT1
float m_fT2
float m_fT3
int m_nEnable
int m_nTextLevel
int m_nUseColorMap
**函数**:
void SetTextLevel(int level)
##### GObjMeshLod
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObjMeshLod
**变量**:
int m_nShowCost
**函数**:
bool AddFace(vec3 p1,vec3 p2,vec3 p3)
void CleanData()
void EndAdd()
bool FindMinCost(float minlevel=0.5)
string GetInfo()
bool ImportRes(string pname,float scale=1.0)
bool ImportStl(string pname,float scale=1.0)
bool RemoveFindEdge()
void SetAddMat(int mat0,int mat1,int mat2)
void SetTexture(var nameorid)
##### ani3d
**类型**:ptrex
**继承**:ptrex/resdatptr/ani3d
**变量**:
ptrex m_pLinkAni
string m_sName
**函数**:
bool Append(string fname)
void CreateFace(float w,float h,float u=1,float v=1)
void CreateSphere(float r,int level=0,float u=1,float v=1)
int FindAniNo(strid aninameid)
int FindMaterial(string pname)
var GetAni(int no=-1)
var GetAniDat(int no)
int GetAniNum()
var GetAniTrack(int anino)
var GetCullSphere(int no=-1)
void GetLinkRes(var& ressz)
var GetMaterial(int no=-1)
int GetMaterialNum()
var GetModel(int no=-1)
int GetModelNum()
var GetNode(int no=-1)
int GetNodeNum()
var GetPerviewData()
var GetPerviewImg()
var GetSkBoneCode()
var GetTag(int no=-1)
var GetUserAgv(string pname)
bool ImportAni(string fname)
bool LinkAni(var actname)
bool Load(string fname)
bool Save(string fname)
bool SetAniDat(var val)
bool SetMaterial(int no,strid paramid,var val)
bool SetPerviewData(var picdata)
void SetTagSz(var tagsz)
void SetUserAgv(string pname,var dat)
##### material
**类型**:ptrex
**继承**:ptrex/material
**变量**:
int OpacityMode:透明模式;enum=(0,'不透明',1,'硬边',2,'Alpha')
vec2 aniUV:颜色图/UV动画
bool bdouble:强制双面
bool bpshadow:高度图/自阴影
bool bwrap:颜色图/环绕
color color:基本颜色
GL_ImgPtr colorimg:颜色图
color emissive:自发光
float f0:镜面反射;range=(0,1)
float lodoffset:颜色图/LOD偏移;range=(-2,2)
var matuseragv:自定义
float metallic:金属度;range=(0,1)
GL_ImgPtr metallicimg:混合贴图?r=金属度,\n可选[g=光滑度,b=F0]
string name:名称
GL_ImgPtr normalimg:法线图
bool normalinvx:法线图/red(x)反转
bool normalinvy:法线图/green(y)反转
float normalmix:法线图/系数;range=(0,1)
float parallax:高度图/偏移系数;range=(0,15)
bool parallaxhigh:高度图/浮雕映射?高精度
GL_ImgPtr parallaximg:高度图?视差偏移
float roughness:粗糙度;range=(0,1)
color wireline:线框颜色
##### GMcTreeMaker
**类型**:class
**继承**:GObj/GMcTreeMaker
**函数**:
bool AddAutoMakeImg(string pimgname,int kindno,var agv)
void AutoMakeByCon(int ix,int iy)
bool LinkDatObj(obj pdat)
bool LoadAutoMakeDat(string pfilename,string pimgpath)
bool PerAutoMakeWd(obj pcon,var kindefv,string pimgpath)
void ReMakeAllGuid()
bool SaveAutoMakeDat(string pfilename)
bool SetAutoMakeKindImg(var agv)
##### GMcWorldObj
**类型**:class
**继承**:GObj/GMcWorldObj
**变量**:
int m_nAutoSaveDelay
obj m_pTreeRoot
var m_vExtVid64
**函数**:
int BarPixel(int x1,int y1,int z1,int x2,int y2,int z2,var smatid)
bool CreateMatImg(int w,int h)
bool CreateWorld(int dep,float subscale=1.0f)
void DestroyWorld()
int FillSphere(vec3 pos,float r,var smatid,int mode=0,int shapemode=0)
void GetAllIndex(var agv)
bool GetData(var& data)
string GetInfo()
var GetMat(int matid)
var GetMatImg(int matid)
int GetMatNum()
var GetMatSz()
var GetMcIndexPt(int i)
var GetMcPtBlock(vec3 pos)
var GetPixel(int x,int y,int z,int mode=0):mode 0=matid,1=val ,2= matid,val,matpage 3=val,matdef
var GetPosBoxIndex(vec3 pos,float len)
void InitLibTex(int w=4096,int h=512)
int IsMatReady()
bool LinkMID(string pmidfilename)
void LinkSvr(var svrpath,var indexbin)
bool LoadFile(string pfilename)
bool SaveFile(string pfilename,int mode=0)
bool SaveLinkBack()
bool SaveWorld()
bool SetData(var data)
int SetMat(int matid,string pname,int defcolor=0xFFCCCCCC,string pimg=NULL,int anispeed=0,var puserv=NULL,int bkind=0)
bool SetMatNormal(int matid,string pimg)
void SetMatReady()
bool SetMatVid(var matst)
bool SetPixel(int x,int y,int z,int matid,int val)
void SetWidgetVid(var widget)
var TestAllocTex(int w,int h)
##### GObj3DPixelMc
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DPixelMc
**变量**:
float m_fCrossDisAdd
float m_fEmptySelectZ
float m_fTestCrossMaxLen
int m_nCacheDataUseSec
int m_nColorOnly
int m_nMatTextureNo
int m_nMaxShowGuid
int m_nShowWidget
obj m_pData
**函数**:
int BarPixel(int x1,int y1,int z1,int x2,int y2,int z2,int smatid)
int FillSphere(vec3 pos,float r,int id,int mode=0,int shapemode=0)
bool FindRayCrossPt(vec3& iv,vec3& idit,float d=0)
bool LinkDatObj(obj pdat)
void OnCtrlLBDown(int x,int y)
void OnDatModi()
void OnMcLibReady()
void RegCollision(int breg=1)
int SetPixel(int x,int y,int z,int smatid,int val=255)
### GObj
**类型**:class
**继承**:GObj
**函数**:
bool AddNoti(strid eveid,obj pobj,strid callfunid):注册消息监听
bool AddParamNoti(strid paramid,obj pobj,strid funid,int bnotiimm=1):增加脚本变量变化通知
int AsyncEmit(strid eveid):异步合并发射消息
void BringToBottom():移动对象次序到低
void BringToTop():移动对象次序到顶
bool CallBack(var fun,var pagv=NULL,int bAsyncRun=0):fun[int,string,script]
bool CallByName(strid funid,var& pcallagv=NULL):按函数名调用,无返回
bool CallByNameWithRet(strid funid,var& pcallagv):按函数名调用,有返回
bool CallUserAgv(strid secid,strid keyid,var pagv=NULL,int bAsyncRun=0)
bool DelNoti(strid eveid,obj pobj,strid callfunid=0):去除消息监听
bool DelParamNoti(strid paramid,obj pobj,strid funid):去除脚本变量变化通知
void DelThis():删除自己()
bool DelUserAgv(strid secid,strid keyid)
void DeleteAllSub():删除所有子对象
int Emit(strid eveid,var pcallagv=NULL):发射消息
int  EmitPackAll():清除所有无效监听
int EventToAllSub(var pevename,var pcallagv=NULL,int btree=0):对子对象广播调用
bool FindFatherParam(strid paramid,var& val):查找父对象变量
int GetAllSubObj(var& pret,int maxsublevel=0):取子对象数组
int GetAllSubObjEx(var& pret,var funname,var paramname,int maxsublevel=0):取过滤子对象数组
int GetAllSubObjNum()const:取所有子对象总数
var GetAllSubSz(var condition=NULL):取子对象数组
string GetClassName()
var GetClassNotes(strid secid=0)
var GetClassNotesEx(strid secid=0)
int GetEmitObjSz(var paramnamesz,var& pret):取消息监听数组
bool GetParam(strid nameid,var& val)
int GetSubObjNum()const:取子对象数目
int GetTraceIconNo():取内部调试的图标号
GVar GetUserAgv(strid secid,strid keyid,var pdef=NULL)
obj GetWndObj():取对象所在窗口
bool IsBaseClass(strid baseid,int bincludescript=0):是否有指定基类
bool IsCanCreateClass(strid classid)
var IsClassCanNotes()
bool IsCondition(var conditionsz)
int IsFunction(strid funid,int funkind=3)
int IsHaveSubObj()const:是否具有子对象
bool IsNoti(strid eveid)const
int IsParam(strid nameid,int paramkind=3):-----------
bool IsStyle(strid styleid)
bool IsSubObj(obj p):是否为子对象
bool IsTimer(strid evenameid)
bool IsUserAgv(strid secid,strid keyid)
void KillTimer(strid evenameid=0)
obj NewObj(var classdef,obj ppFather)
bool NotiParamChged(strid nameid,var pval)
bool RunScriptFile(string pfilename)
bool SafeDelObj(obj p):测试删除对象(obj)返回是否删除
void SetClassNotes(strid secid,var agv)
bool SetObjFather(obj p):指定父对象
bool SetParam(strid nameid,var val,int bnoti=1)
bool SetTimer(float delaysec,strid evenameid,var pagv=NULL,int times=0)
bool SetTraceObj(obj p)
void SetUserAgv(strid secid,strid keyid,var val)
bool UseStyle(var styledef)
### GObjUndo
**类型**:class
**继承**:GObj/GObjUndo
**变量**:
int m_UndoNum
**函数**:
bool AddUndo(int opver,strid opkind,var opkey,var opdat)
void Destroy()
bool EndUndoOp(int opver)
int PerUndoOp(obj plink,strid nameid)
bool TryUndo()
### GWebLink
**类型**:class
**继承**:GObj/GWebLink
**变量**:
int m_bTrace
int m_nPort
string m_sHttpHead
string m_sUrl
var m_vRetHead
**函数**:
bool Post(string postdata)
void SetCtrlFun(string pfunname)
bool SetNoti(string pfun)
bool SetUrl(string purl)
#### GMIDFileObj
**类型**:class
**继承**:GObj/GMIDFileObj
**函数**:
bool Clean()
void Close()
int DelKey(var key0,int k1=-1,int k2=-1)
bool DelVar(var keyv)
int GetFileLen()
int GetKeyNum()
int64 GetNewKey0()
int GetUserFlag(int no)
bool IsHaveKey(var keyv)
bool IsOpen()
var ListKey(var key0,int k1=-1,int k2=-1)
bool Open(string pcachefilename,int breadnoly=0)
var ReadAllAsVar(var key0,int k1=-1,int k2=-1)
bool ReadVar(var keyv,var& v)
void SetUserFlag(int no,int flag)
bool WriteVar(var keyv,var v,int ziplevel=4)
#### GObjLZ4File
**类型**:class
**继承**:GObj/GObjLZ4File
**变量**:
var m_vExtInfo
**函数**:
bool AddBin(var bin,string destname,int date=0)
bool AddFile(string filename,string destname)
bool AddText(var strv,string destname,int utf8=1,int date=0)
void Begin()
bool End(string pfilename)
#### GObjVDisk
**类型**:class
**继承**:GObj/GObjVDisk
**函数**:
void Close()
bool DeleteFile(string pfilename)
var GetFile(string fname)
bool IfHaveFile(string fname, int date=0, int len=0)
var ListDirEx(string listpath,int binfo=0)
bool LoadFileBin(var& pretbin,string pfilename)
bool LoadFileBinRange(var& pretbin,string pfilename,var startpos,int len)
bool OpenVDisk(string pfilename,string mappath,int breadonly=0,int badd=1)
bool PreWritePath(string path)
bool RemoveDir(string path)
bool SaveFileBin(var& pwbin,string pfilename,int filetime=0)
bool SaveFileBinRange(var& pwbin,string pfilename,var startpos)
bool SetFileTime(string pfilename,int filetime)
#### GObjZipFile
**类型**:class
**继承**:GObj/GObjZipFile
**函数**:
bool AddFile(string filename,string destname=NULL)
void BeginZip()
void Close()
bool EndZip(string pfilename,string pass=NULL)
var GetFileBin(string pfilename)
var GetZipInfo(int pos)
int OpenZip(string pfilename,string pass=NULL)
#### GNetFileObj
**类型**:class
**继承**:GObj/GNetFileObj
**变量**:
int m_FileDate
int64 m_FileSize
int64 m_TransLen
float m_fTransSpeed
string m_sLocName
string m_sUrlName
var m_vDownInfo
var m_vPostDest
var m_vUserAgv
**函数**:
bool GetDown(var psvrlink,strid svrfunid,string purl,string plocname)
var GetDownInfo()
int64 GetFileSize()
int GetFileTime()
float GetTransSpeed()
bool OnFileInfo(var info)
bool PerFileSvr(string pname,string plocname,int isupmode=0)
bool SetFileTime(int time)
void SetNoti(obj ptr,strid okfun,strid errfun,strid perfun=0)
bool StartDown(var postdest,string purl,string plocname,var fsize,int fdate)
#### GSocket
**类型**:class
**继承**:GObj/GSocket
**变量**:
int m_nPing:当前的ping值
int m_nStrBinLen:字符串编码模式二进制Cmd
int m_nStrCode:字符串编码模式;0 is unicode默认,1 is UTF8,2 is GBK
**函数**:
void Close():关闭socket
void EnableMon(int bmon=1)
int GetAddress():取连接整数IP
string GetAddressString():取连接IP地址
int GetOnDataMode():取当前消息处理模式
bool GetReadCache(var& getbin,int getlen=0,int bdel=0)
bool GetStrBinInfo(int &getsize,int &total):取字符串编码模式下数据长度
bool IsConnected():是否已经连接
bool SendBinDirect(var& binv):直接发送二进制
bool SendLine(string pMsg):发送字符串,模式受m_nStrCode控制
void SetOnDataMode(int mode):设置消息处理模式
#### GSocketC
**类型**:class
**继承**:GObj/GSocket/GSocketC
**变量**:
int m_nPort
string m_sServName
**函数**:
void CloseSocket()
bool Connect(string pservername, int iport,string perrconnecteve=NULL,var& perragv=NULL)
void OnConnectOutTime():连接超时
void Relink()
void SetMaxReadTime(int t)
void TestBreak()
#### GSocketS
**类型**:class
**继承**:GObj/GSocketSBase/GSocketS
**函数**:
int GetBindAddress()
int GetSocketNum()
bool IsStart()
void SetLimit(int max)
bool StartServer(int port,int bautoscanport=1,string pBindAddStr=NULL,int bReuseaddr=0):返回是否成功
#### GSocketSBase
**类型**:class
**继承**:GObj/GSocketSBase
**函数**:
var GetAllRec()
int GetPort():返回端口号
void SetAutoPingDelay(int delay)
void SetRecClass(obj p,string pclassname=NULL):设置联入的GSocket父对象和派生类名
#### GSocketUdp
**类型**:class
**继承**:GObj/GSocketUdp
**变量**:
int m_nPort
**函数**:
bool BindPort(int port=0,int scanenum=5,string pbindip=NULL)
int GetIpAddress(string paddress)
bool SendTo(int ip,int port,int cmdid,var pagv=NULL)
#### GVNetObj
**类型**:class
**继承**:GObj/GVNetObj
**函数**:
void AddLink(int64 mac,var paddr,var agv)
void OnVAddressBreak(int errkind,var agv)
void ToC(strid fun,var pagv=NULL)
#### GWebFile
**类型**:class
**继承**:GObj/GWebFile
**变量**:
int m_nDownNum
int m_nStatus
obj m_pNoti
string m_sHeadEx
string m_sLoc
string m_sTempFile
string m_sUrl
**函数**:
void CheckDown()
bool DownFile(string purl,string ploc,string ptmpfile=NULL,int suboutsec=3)
void DownFileErr(string pmsg)
void OnData(int l,int total,int uflag)
void OnDataReady(var retv)
void OnDownNetErr(int flag,string pmsg,int uflag)
void OnFileReady()
void SetMaxDown(int n=8,int subsizekb=512)
#### csvr
**类型**:namespace
**继承**:csvr:task
**函数**:
void AddSelfIpSz(string ipport)
int AutoStart(int port=1000,int scanenum=100,string pbindip=NULL)
bool BindSvrAddress(string path,string ipadd)
var GetInfo(strid kind,var pagv=NULL)
int GetLinkStatus(strid aid,int bautolink=1)
string GetSelfIp()
var GetSelfIpSz()
bool IsStart()
var MakePtr(var pobj,var address)
bool OpenHole(string pipport)
bool RegSvr(obj pobj,string pname)
var SelectIpSz(var ipsz)
bool Start(int port=0,string pbindip=NULL)
var call(strid aid,strid svrid,strid fid,var pagv=NULL,int outsec=10)
var callptr(var psvr,strid fid,var pagv=NULL,int outsec=10)
bool post(var netaddress,strid fid,var pagv=NULL)
bool send(strid aid,strid svrid,strid fid,var pagv=NULL)
#### csvr::addr
**类型**:ptrex
**继承**:ptrex/csvr::addr
**函数**:
var Clone(var netobj64,int newvlink=0)
var GetAddress(var pnetobj64=NULL)
int GetIdelMax()
string GetIp()
string GetIpPort()
var GetNetObj()
int GetRBufSize()
int GetWBufSize()
bool InitBySvrIP(string pinfo):svrname::ip[:port]
int IsLink()
int IsReady()
bool LinkSvr(var pobj,var ip)
bool SendCall(strid funid,var pagv=NULL,var pnetobj64=NULL)
void SetIdelMax(int maxsec)
void SetNotiObj(obj pobj,int mask=1)
#### netapi
**类型**:namespace
**继承**:netapi:task
**函数**:
var FindSvr(string psvrname)
var call(string svrname,strid funid,var pagv=NULL,int outsec=2)
void post(string svrname,strid funid,var pagv=NULL)
void send(string svrname,strid funid,var pagv=NULL)
#### web
**类型**:namespace
**继承**:web:task
**函数**:
var Get(string purl)
var GetFile(string purl,string ploc,obj pnoti)
var GetRange(string purl,int st,int end)
var Post(string purl,string postdata)
void SetHttpHead(string pheadex)
void SetMaxIdel(int maxidel=8)
#### GBoxShowApp
**类型**:class
**继承**:GObj/GObjShow/GObj2DWnd/GBoxShowApp
**变量**:
float m_fIMEPopH
**函数**:
void CloseApp()
var FindScrPtWnd(vec2 pt)
#### GObj2DSandBox
**类型**:class
**继承**:GObj/GObjShow/GObj2DSandBox
**变量**:
int m_nLaunchAppliction
int m_nShellOpenDoc
obj m_pSandApp
**函数**:
obj CreateSandAppObj(int b3d=0)
bool DefMacro(string pkey,var val)
var GetIncludeFiles()
obj GetResCtrl()
var GetRootClassPtr()
bool GetScriptClassInfo(var& ret,var pobj)
obj GetShowRoot()
bool IsIncludeFile(int fid)
bool LoadScript(string pstartname)
obj NewSandBoxObj(strid classnameid,obj ppFather)
bool Reset()
var SeekFileClassFun(int fid,int line,int col)
bool Start()
#### GObj3DSandBox
**类型**:class
**继承**:GObj/GObjShow/GObj3DShow/GObj3DSandBox
**变量**:
obj m_pSandApp
**函数**:
obj CreateSandAppObj(int b3d=0)
var GetIncludeFiles()
obj GetResCtrl()
var GetRootClassPtr()
bool GetScriptClassInfo(var& ret,var pobj)
var GetScriptRes()
obj GetShowRoot()
var GetSystemVID()
bool IsIncludeFile(int fid)
bool LoadScript(string pstartname0,string pstartname1=NULL,string pstartname2=NULL)
obj NewSandBoxObj(strid classnameid,obj ppFather)
bool Reset()
var SeekFileClassFun(int fid,int line,int col)
bool Start(int b3d=0)
#### GObjSandBox
**类型**:class
**继承**:GObj/GObjSandBox
**函数**:
bool CompileExp(string pext)
#### GSandApp2DWnd
**类型**:class
**继承**:GObj/GObjShow/GObj2DWnd/GSandApp2DWnd
#### GSandAppWnd
**类型**:class
**继承**:GObj/GObjShow/GSandAppWnd
**函数**:
string GetText()
void SetText(string pstr)
bool SetWinIcon(string piconfilename):设置窗口图标
#### GSandBoxWinApp
**类型**:class
**继承**:GObj/GObjShow/GObj2DWnd/GBoxShowApp/GSandBoxWinApp
**函数**:
int UpdateGBoxExe(string pexename)
#### locapi
**类型**:namespace
**继承**:locapi:task
**函数**:
int IsSvr(strid nameid)
int Post(strid nameid,strid funid,var pagv=NULL)
int RegSvr(strid nameid,obj pobj)
## style SysKeyMap
**类型**:class
**继承**:
**函数**:
SysKeyMap:nil
### style DNSSvrStyle
**类型**:class
**继承**:
**变量**:
DNSSvrStyle int:nil
DNSSvrStyle ptrex:nil
DNSSvrStyle string:nil
DNSSvrStyle string:nil
DNSSvrStyle string:nil
DNSSvrStyle string:nil
DNSSvrStyle string:nil
**函数**:
DNSSvrStyle:nil
DNSSvrStyle:nil
DNSSvrStyle:nil
DNSSvrStyle:nil
DNSSvrStyle:nil
### class SysBoot:netDownPathDlg
**类型**:class
**继承**:
**变量**:
SysBoot string:nil
**函数**:
SysBoot:nil
SysBoot:nil
SysBoot:nil
### class SysNetFile
**类型**:class
**继承**:
**变量**:
SysNetFile float:nil
SysNetFile float:nil
SysNetFile int:nil
SysNetFile obj:GObjText:nil
SysNetFile var:nil
SysNetFile obj:GObjText:nil
SysNetFile obj:GObjShape:nil
SysNetFile obj:GObjText:nil
SysNetFile obj:nil
**函数**:
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
SysNetFile:nil
### class dnsFile
**类型**:class
**继承**:
**变量**:
dnsFile string:nil
dnsFile var:nil
**函数**:
dnsFile:nil
dnsFile:nil
dnsFile:nil
dnsFile:nil
dnsFile:nil
dnsFile:nil
dnsFile:nil
### class miniBtn
**类型**:class
**继承**:
**变量**:
miniBtn var:nil
**函数**:
miniBtn:nil
miniBtn:nil
miniBtn:nil
miniBtn:nil
### class miniCon
**类型**:class
**继承**:
**函数**:
miniCon:nil
miniCon:nil
miniCon:nil
miniCon:nil
### class miniOutTxt
**类型**:class
**继承**:
**函数**:
miniOutTxt:nil
miniOutTxt:nil
miniOutTxt:nil
miniOutTxt:nil
### class miniProg
**类型**:class
**继承**:
**变量**:
miniProg float:nil
miniProg int:nil
miniProg string:nil
**函数**:
miniProg:nil
miniProg:nil
miniProg:nil
miniProg:nil
### class netAPISvr:miniCon:DNSSvrStyle
**类型**:class
**继承**:
**变量**:
netAPISvr obj:GObjText:nil
netAPISvr obj:miniOutTxt:nil
netAPISvr var:nil
**函数**:
netAPISvr:nil
netAPISvr:nil
netAPISvr:nil
netAPISvr:nil
netAPISvr:nil
netAPISvr:nil
### class netDownPathDlg
**类型**:class
**继承**:
**变量**:
netDownPathDlg int64:nil
netDownPathDlg int:nil
netDownPathDlg int:nil
netDownPathDlg int64:nil
netDownPathDlg int:nil
netDownPathDlg int64:nil
netDownPathDlg obj:nil
netDownPathDlg obj:miniBtn:nil
netDownPathDlg obj:miniOutTxt:nil
netDownPathDlg obj:miniProg:nil
netDownPathDlg ptrex:csvr::addr:nil
netDownPathDlg obj:TextTitel:nil
netDownPathDlg string:nil
netDownPathDlg string:nil
netDownPathDlg string:nil
netDownPathDlg var:nil
**函数**:
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
netDownPathDlg:nil
#### class TextTitel
**类型**:class
**继承**:netDownPathDlg
##### class m_pOut/$miniOutTxt:miniOutTxt
**类型**:class
**继承**:netDownPathDlg
