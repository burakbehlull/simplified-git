import os
import xml.etree.cElementTree as ET
dosyayi_cek = ET.parse('settings.xml')
veriyi_al = dosyayi_cek.getroot()

for workplace in veriyi_al.iter('workplace'):
    wp = workplace.text
    disk = wp[0:2]
for dftdf in veriyi_al.iter('downloadfile'):
    dwnFile = dftdf.text
    dwnDisk = dwnFile[0:2]
help_list = ["Diğer Komutlar |",
            "yardım -2", 
            "yardım -3", 
            "yardım -4", 
            "yardım -sc"
            "\n\t",
            "Giriş | login", "Giriş Kontrol | lc",
            "Giriş Bilgileri Değiştirme | gcra",
            "Dosya Yükleme | y",
            ".gitignore | gi",
            "wd | Çalışma ve indirme alanının konumunu gösterir.",
            "wd return | Konsol üzerinde günceller.",
            "wd update | Çalışma ve İndirme Alanını Günceller",
            "settings.xml | Ayarlar dosyasının içerisini değiştirirsiniz."
            "gitignore generetor | gg.exe",
            "\n\t",
            "git init | init",
            "git commit -m [mesaj]",
            "git log | l",
            "git status | st",
            "git add all * | add all",
            "git add -file-| add -file-",
            "git clone | i, indir",
            "git pull | gl",
            "gitk | k",
            "git show | sh",
            "git diff | diff",
            "\n\t",
            "git tag (sürüm adı) | tag",
            "git tag -l -n | tagln",
            "git tag -m (mesaj) | tagm",
            "git archive --output (DosyaAdı).zip (branchName) | save "
            ]
helpTwo_list = ["git rm | rm",
            "git rm --cached | rmc",
            "git commit --amend -m | cam",
            "git log -n -number- | logn",
            "git diff (commmitID)..(CommitID) | diffw",
            "git revert (CommitID) | rev",
            "git reset --hard (CommitID) | res",
            "git branch | br -sh",
            "git branch (branchName) | br -c",
            "git checkout (branchName) | ch",
            "git checkout -b (branchName) | br -ch",
            "git checkout -D (branchName) | ch -d"]
helpThree_list = ["git stash | stash",
            "git stash list | stash -l",
            "git stash clear | stash -c",
            "git stash pop | stash -p",
            "git stash apply | stash -a",
            "git merge --squash (branchName) | mr -sqn",
            "git merge (branchName) | mrn",
            "git merge --abort | mr -abn",
            "git rebase (branchName) | rebase"
            "git reflog | rf",
            "git mv (eski ad) (yeni ad) | mv",
            "git log --follow (Dosya Adı) | lf",
            "git blame (Dosya Adı) | bl"]
helpFour_list = ["git push | gitp ",
            "git push origin master | gitp -o -m",
            "git push [args] | gitp -a",
            "git remote | gitr",
            "git remote -v | gitr -v"
            ]
helpSystemCodes = ["Dosya Oluşturma| do, mk", 
            "dir | d",
            "copy | cp (oldFile) (newFile)",
            "cls | clear"]
def yardim():
    print("\t --YARDIM 1--")
    for i in help_list:
        print("\t", i)
    return " "
def yardim2():
    print("\t --YARDIM 2--")
    for i in helpTwo_list:
        print("\t", i)
    return " "
def yardim3():
    print("\t --YARDIM 3--")
    for i in helpTwo_list:
        print("\t", i)
    return " "
def yardim4():
    print("\t --YARDIM 4--")
    for i in helpFour_list:
        print("\t", i)
    return " "
def yardımSistemKodlari():
    print("\t --YARDIM 5--")
    for i in helpSystemCodes:
        print("\t", i)
    return " "

def git_pull():
    global disk
    global wp
    pull = lambda: os.system(f'{disk} & cd {wp} & git pull')
    pull()
    return "\t ***"


def wpdW_control():
    global wp
    global dwnFile
    print(f"workplace: {wp}")
    print(f"download file: {dwnFile}")
    return "\t ***"
def wdReturn():
    global wp
    global dwnFile
    pullWi = ET.parse('settings.xml')
    getDate = pullWi.getroot()
    for retwp in getDate.iter('workplace'):
        wpNew = retwp.text
        disk = wp[0:2]
    for retdf in getDate.iter('downloadfile'):
        dwnFileNew = retdf.text
        dwnDisk = dwnFileNew[0:2]
    wp = wpNew
    dwnFile = dwnFileNew
    print(f"Güncellendi:\n\tWorkplace: {wp}\n\tDownloadplace: {dwnFile}")
    return "\t ***"
def wdUpdateRom():
    global wp
    global dwnFile
    choosess = int(input('1- Çalışma alanını güncelleme\n2- İndirme Alanaını Güncelleme\n3-Çalışma ve İndirme Alanı Ayarlama, -Çıkış\nPath: '))
    if choosess == 1:
        wpUp = input('Çalışma Alanı Yolu: ')
        disk = wpUp[0:2]
        wp = wpUp
        print("Workplace: "+ wp)
    elif choosess== 2:
        dfUp = input('İndirme Alanı Yolu: ')
        dwnDisk = wpUp[0:2]
        dwnFile = wpUp
        print("DownloadFile: "+ dwnFile)
    elif choosess==3:
        wpUp = input('Çalışma Alanı Yolu: ')
        dfUp = input('İndirme Alanı Yolu: ')
        disk = wpUp[0:2]
        wp = wpUp
        dwnDisk = wpUp[0:2]
        dwnFile = wpUp
        print("Workplace: "+ wp)
        print("DownloadFile: "+ dwnFile)
    elif choosess==0:
        pass
    else:
        print('Seçim yapmadınız.')
    return "\t ***"
def settings():
    chooseSet = int(input('1-Çalışma ve İndirme Yolu, 2- Çalışma Yolu 3-İndirme Yolu, 0-Çıkış\nChoose: '))
    if chooseSet == 1:
        xwP = input('Çalışma Yolu: ')
        xDf = input('İndirme Yolu: ')
        with open('settings.xml','w') as sett:
            sett.write(f"<?xml version='1.0' encoding='UTF-8'?>\n<ayarlar>\n<on-off>on</on-off>\n<workplace>{xwP}</workplace>\n<downloadfile>{xDf}</downloadfile>\n</ayarlar>")
            sett.close()
            print("Dosya başarıyla yazdırıldı.")
            wdReturn()
    elif chooseSet==2:
        global dwnFile
        xwP = input('Çalışma Yolu: ')
        with open('settings.xml','w') as sett:
            sett.write(f"<?xml version='1.0' encoding='UTF-8'?>\n<ayarlar>\n<on-off>on</on-off>\n<workplace>{xwP}</workplace>\n<downloadfile>{dwnFile}</downloadfile>\n</ayarlar>")
            sett.close()
            print("Dosya başarıyla yazdırıldı.")
            wdReturn()
    elif chooseSet==3:
        global wp
        xDf = input('İndirme Yolu Yolu: ')
        with open('settings.xml','w') as sett:
            sett.write(f"<?xml version='1.0' encoding='UTF-8'?>\n<ayarlar>\n<on-off>on</on-off>\n<workplace>{wp}</workplace>\n<downloadfile>{xDf}</downloadfile>\n</ayarlar>")
            sett.close()
            print("Dosya başarıyla yazdırıldı.")
            wdReturn()
    elif chooseSet==0:
        pass
    else:
        print('Bir şey seçmediniz.')
    return "\t ***"
def dosyaolustur():
    global disk 
    global wp
    dosya_ismi = input("Dosya Adı: ")
    dosya_olusturucu = lambda: os.system(f'{disk} & cd {wp} & mkdir {dosya_ismi}')
    dosya_olusturucu()
    return "\t ***"
def workplace_dir():
    global disk 
    global wp
    wp_dir = lambda: os.system(f"{disk} & cd {wp} & dir")
    wp_dir() 
def clear():
    cls = lambda: os.system("cls")
    cls()
    return "\t ***"
def copy():
    eskiad = input("Dosya Adı: ")
    yeniad = input("Dosyanın Yeni Adı ")
    copy_ = lambda: os.system(f"{disk} & cd {wp} & copy {eskiad} {yeniad}")
    copy_()
    return "\t ***"
def gcra():
    print("Lütfen değiştireceğiz, username ve emailinizi giriniz.")
    username = input("username: ")
    email = input("email: ")
    login_username = lambda: os.system(f"git config --global --replace-all user.name  \"{username}\"")
    login_email = lambda: os.system(f"git config --global --replace-all user.email \"{email}\"")
    login_username()
    login_email()
    return "\t ***"

def cd():
    cd = lambda: os.system("cd")
    cd()
    return "\t ***"
def git_login():
    username = input("username: ")
    email = input("email: ")
    comet_control = email.find("@")
    if comet_control > 0:
        login_username = lambda: os.system(f"git config --global user.name  \"{username}\"")
        login_email = lambda: os.system(f"git config --global user.email \"{email}\"")
        login_username()
        login_email()
        print("İşlem tamamlandı.")
    else:
        print("Lütfen içinde @ olan bir email giriniz.")
    return "\t ***"
def git_login_control():
    control_username = lambda: os.system(f"git config --global user.name")
    control_email = lambda: os.system(f"git config --global user.email")
    control_username()
    control_email()
    return "\t ***"
def git_init():
    global disk 
    global wp
    try:
        run_init = lambda: os.system(f"{disk} & cd {wp} & git init")
        run_init()
    except Exception as e:
        print("Hata: ", e)
    else:
        print("İşlem Tamamlandı.")
    return "\t ***"
def git_commit():
    global disk 
    global wp
    message = input("Mesaj: ")
    commit_message_send = lambda: os.system(f"{disk} & cd {wp} & git commit -m \"{message}\"")
    commit_message_send()
    print(f"{message}, başarıyla kaydedildi.")
    return "\t ***"
def git_log():
    global disk 
    global wp
    log = lambda:os.system(f"{disk} & cd {wp} & git log")
    log()
    return "\t ***"
def git_status():
    global disk 
    global wp
    status = lambda:os.system(f"{disk} & cd {wp} & git status")
    status()
    return "\t ***"
def git_blame():
    global disk
    global wp
    fileName = input("Dosya Adı: ")
    blame = lambda: os.system(f" {disk} & cd {wp} & git blame {fileName}")
    blame()
    
def git_add_all():
    global disk 
    global wp
    add_all = lambda:os.system(f"{disk} & cd {wp} & git add *")
    add_all()
    return "\t ***"
def git_add():
    fileName = input("Dosya adı: ")
    git_Add = lambda: os.system(f"{disk} & cd {wp} & git {fileName}")
    git_Add()
    return "\t ***"
def indir():
    link = input("link: ")
    endsing = link.endswith("/")
    if endsing == True:
        print("Lütfen linkin sonundaki / siliniz.")
    else:
        _indir_ = lambda: os.system(f"{dwnDisk} & cd {dwnFile} & git clone {link}.git")
        _indir_()
    return "\t ***"
def y():
    choose = int(input("Varsayılan Yol > 1\nFarklı Yol Tanımlamak İçin > 2\n>"))
    link = input("Link: ")
    message = input("Mesaj: ")
    endsing = link.endswith("/")
    if choose == 1:
        if endsing == True:
            print("Lütfen sondaki / siliniz")
        else:
            global wp
            global disk
            init = lambda: os.system(f"{disk} & cd {wp} & git init")
            init()
            add_all = lambda: os.system(f"{disk} & cd {wp} & git add *")
            add_all()
            remote_add_origin = lambda: os.system(f"{disk} & cd {wp} & git remote add origin {link}.git")
            remote_add_origin()
            commit = lambda: os.system(f"{disk} & cd {wp} & git commit -m \"{message}\"")
            commit()
            _push_ = lambda: os.system(f"{disk} & cd {wp} & git push origin master")
            _push_()
            print("İşlem  tamamlandı.")
    elif choose == 2:
        wp = input("Yol: ")
        disk = wp[0:2]
        if endsing == True:
            print("Lütfen sondaki / siliniz")
        else:
            init = lambda: os.system(f"{disk} & cd {wp} & git init")
            init()
            add_all = lambda: os.system(f"{disk} & cd {wp} & git add *")
            add_all()
            remote_add_origin = lambda: os.system(f"{disk} & cd {wp} & git remote add origin {link}.git")
            remote_add_origin()
            commit = lambda: os.system(f"{disk} & cd {wp} & git commit -m \"{message}\"")
            commit()
            _push_ = lambda: os.system(f"{disk} & cd {wp} & git push origin master")
            _push_()
    else:
        print("Lütfen geçerli bir seçenek giriniz.")
    return "\t ***"
def gitk():
    global disk 
    global wp
    k = lambda: os.system(f"{disk} & cd {wp} & gitk")
    k()
    return "\t ***"
def git_push():
    global disk 
    global wp
    gitpush = lambda: os.system(f"{disk} & cd {wp} & git push")
    gitpush()
    return "\t ***"
def git_show():
    global disk 
    global wp
    show = lambda: os.system(f"{disk} & cd {wp} & git show")
    show()
    return "\t ***"
def git_diff():
    global disk 
    global wp
    diff = lambda: os.system(f"{disk} & cd {wp} & git diff")
    diff()
    return "\t ***"
def git_reflog():
    global disk 
    global wp
    reflog = lambda: os.system(f"{disk} & cd {wp} & git reflog")
    reflog()
    return "\t ***"
def git_mv():
    global disk
    global wp
    yeniad = input("Yeni Ad: ")
    eskiad = input("Eski Ad: ")
    mv_ = lambda: os.system(f"{disk} & cd {wp} & git mv {yeniad} {eskiad}")
    mv_()
    return "\t ***"
def git_tag():
    global disk
    global wp
    tagName = input("Tag adını belirleyin: ")
    tag = lambda: os.system(f"{disk} & cd {wp} & git tag {tagName}")
    tag()
    return "\t ***"
def git_tag_ln():
    global disk
    global wp
    tagln = lambda: os.system(f"{disk} & cd {wp} & git tag -l -n")
    tagln()
    return "\t ***"
def git_tag_message():
    global disk
    global wp
    tagMessage = input("Tag Mesajı: ")
    tagm = lambda: os.system(f"{disk} & cd {wp} & git tag -m {tagMessage}")
    tagm()
    return "\t ***"
def git_rm():
    global disk 
    global wp
    dosya = input("Silenecek Dosya: ")
    rm = lambda: os.system(f"{disk} & cd {wp} & git rm {dosya}")
    rm()
    return "\t ***"
def git_rm_cached():
    global disk 
    global wp
    dosya = input("İzlenimden Kaldıralacak Dosya: ")
    rm_cached = lambda: os.system(f"{disk} & cd {wp} & git rm --cached {dosya}")
    rm_cached()
    return "\t ***"
def gitignore():
    global wp
    global disk
    print("Eğer bu dosya ise <here>, \n başka bir dosya belirtecekseniz: <other> yazınız")
    secenekler = input("> ")
    if secenekler == "here":
        print("Her aşağı satır için <?> yazınız. \n Lütfen <?> yazarken sağ ve solda boşluk bırakınız, \n yoksa aşağı satıra geçmez.")
        x = input(".gitignore: ")
        y = x.replace(" <?> ", "\n")
        with open('.gitignore','w') as ignore:
            ignore.write("easy-git.exe\nsettings.xml \n" + y)
        ignore.close()
    else:
        print("Lütfen, her yol belirtiken sonuna / koymayı unutmayınz.")
        print("Her aşağı satır için <?> yazınız. \n Lütfen <?> yazarken sağ ve solda boşluk bırakınız, \n yoksa aşağı satıra geçmez.")
        x = input(".gitignore: ")
        y = x.replace(" <?> ", "\n")
        ex = lambda: os.system(f"{disk} & cd {wp}")
        ex()
        
        w = f"{wp}/"
        with open(w+'.gitignore','w') as ignore:
            ignore.write("easy-git.exe\nsettings.xml \n" + y)
        ignore.close()
        xyz = lambda: os.system(f"{disk} & cd {wp}")
        xyz()
    return "\t ***"
def commit_amend_m():
    global wp
    global disk
    message = input("mesaj: ")
    amend = lambda: os.system(f"{disk} & cd {wp} & git commit --amend -m \"{message}\"")
    amend()
    return "\t ***"
def git_archive_output():
    global wp
    global disk
    branchName = input("BranchName:  ")
    fileName = input("Oluşturulacak Zip Adı:  ")
    arc = lambda: os.system(f"{disk} & cd {wp} & git archive --output {fileName}.zip {branchName}")
    arc()
    return "\t ***"
def git_log_args():
    global wp
    global disk
    args = int(input("(1-numbers): "))
    log_args = lambda: os.system(f"{disk} & cd {wp} & git log -n {args}")
    log_args()
    return "\t ***"
def diff_commitID():
    global wp
    global disk
    gitlog = lambda: os.system(f"{disk} & cd {wp} & git log") 
    gitlog()
    commitID_1 = input("1. commitID: ")
    commitID_2 = input("2. commitID: ")
    
    diff_views = lambda: os.system(f"{disk} & cd {wp} & git diff {commitID_1}..{commitID_2}")
    diff_views()
    return "\t ***"
def git_revert():
    global wp
    global disk
    gitlog = lambda: os.system(f"{disk} & cd {wp} & git log") 
    gitlog()    
    commitID = input("CommitID: ")
    revert = lambda: os.system(f"{disk} & cd {wp} & git revert {commitID}")
    revert()
    return "\t ***"
def git_resetHARD():
    global wp
    global disk
    gitlog = lambda: os.system(f"{disk} & cd {wp} & git log") 
    gitlog()
    commitID = input("CommitID: ")
    resetHARD = lambda: os.system(f"{disk} & cd {wp} & git reset --hard {commitID}")
    resetHARD()
    return "\t ***"
def branch_create():
    global wp
    global disk
    branchName = input("branchName: ")
    branched = lambda: os.system(f"{disk} & cd {wp} & git branch {branchName}")
    branched()
    return "\t ***"
def git_log_follow():
    global wp
    global disk
    fileName = input("Dosya adı: ")
    logFollow = lambda: os.system(f"{disk} & cd {wp} & git log --follow {fileName}")
    logFollow()
    return "\t ***"
def git_checkout():
    global wp
    global disk
    branchName = input("branchName: ")
    branch_switch = lambda: os.system(f"{disk} & cd {wp} & git checkout {branchName}")
    branch_switch()
    return "\t ***"
def checkout_b():
    global wp
    global disk
    branchName = input("branchName: ")
    checkoutB = lambda: os.system(f"{disk} & cd {wp} & git checkout -b {branchName}")
    checkoutB()
    return "\t ***"
def checkout_d():
    global wp
    global disk
    branchName = input("delete to branchName: ")
    checkoutD = lambda: os.system(f"{disk} & cd {wp} & git branch -D {branchName}")
    checkoutD()
    return "\t ***"
def git_stash():
    global wp
    global disk
    stash = lambda: os.system(f"{disk} & cd {wp} & git stash")
    stash()
    return "\t ***"
def git_stash_list():
    global wp
    global disk
    stashL = lambda: os.system(f"{disk} & cd {wp} & git stash list")
    stashL()
    return "\t ***"
def git_stash_clear():
    global wp
    global disk
    stashC = lambda: os.system(f"{disk} & cd {wp} & git stash clear")
    stashC()
    return "\t ***"
def git_stash_pop():
    global wp
    global disk
    stashP = lambda: os.system(f"{disk} & cd {wp} & git stash pop")
    stashP()
    return "\t ***"
def git_stash_apply():
    global wp
    global disk
    cID = input("ID: ")
    stashP = lambda: os.system(f"{disk} & cd {wp} & git stash apply {cID}")
    stashP()
    return "\t ***"
def git_branch_show():
    global wp
    global disk
    bs = lambda: os.system(f"{disk} & cd {wp} & git branch")
    bs()
    return "\t ***"
def git_merge_squash():
    global wp
    global disk
    branch = input("branchName: ")
    squash = lambda: os.system(f"{disk} & cd {wp} & git merge --squash {branch}")
    squash()
    return "\t ***"
def git_merge():
    global wp
    global disk
    branch = input("branchName: ")
    merge = lambda: os.system(f"{disk} & cd {wp} & git merge {branch}")
    merge()
    return "\t ***"
def git_merge_abort():
    global wp
    global disk
    abort = lambda: os.system(f"{disk} & cd {wp} & git merge --abort")
    abort()
    return "\t ***"
def git_rebase():
    global wp
    global disk
    branch = input("branchName: ")
    rb = lambda: os.system(f"{disk} & cd {wp} & git rebase {branch}")
    rb()
    return "\t ***"
def gitPush_oM():
    o_M = lambda: os.system(f'{disk} & cd {wp} & git push origin master')
    o_M()
    return "\t ***"
def gitPush_Args():
    args = input('Genellikle origin master olarak kullanılır\nPath: ')
    sendArgs = lambda: os.system(f"{disk} & cd {wp} & git push {args}")
    sendArgs()
    return "\t ***"
def gitRemote():
    remote = lambda: os.system(f"{disk} & cd {wp} & git remote")
    remote()
    return "\t ***"
def gitRemoteV():
    remoteV = lambda: os.system(f"{disk} & cd {wp} & git remote -v")
    remoteV()
    return "\t ***"
def gitpull_Args():
    args = input('Genellikle origin master olarak kullanılır\nPath: ')
    Args = lambda: os.system(f"{disk} & cd {wp} & git ull {args}")
    Args()
    return "\t ***"
def producer():
    print('Yapımcı: Burak\nGithub: 31000s\nİnstagram: 3.10.00s')
    return "\n ***"  
def exeGG():
    myexe = lambda: os.system('start gg.exe')
    myexe()
    return ""
def default():
    try:
        cmd = lambda: os.system(f'{disk} & cd {wp} & {komut}')
        cmd()
    except Exception as err:
        print(err)
    else:
        pass
    return "\t ***"
komutlar = {
    "gg.exe": exeGG,
    "yardım": yardim,
    "help": yardim,
    
    "yardım -2": yardim2,
    "yardım-2": yardim2,
    "help -2": yardim2,
    "help-2": yardim2,
    
    "yardım -3": yardim3,
    "yardım-3": yardim3,
    "help -3": yardim3,
    "help-3": yardim3,
    
    "yardım -4": yardim4,
    "yardım-4": yardim4,
    "help -4": yardim4,
    "help-4": yardim4,
    "yardım -sc": yardımSistemKodlari,
    "yardım-sc": yardımSistemKodlari,
    "help -sc": yardımSistemKodlari,
    "help-sc": yardımSistemKodlari,
    #/help
    "login control": git_login_control,
    "lc": git_login_control,
    "gcra": gcra,
    "i": git_init,
    "init": git_init,
    "login": git_login,
    "message": git_commit,
    "msg": git_commit,
    "c": git_commit,
    "log": git_log,
    "l": git_log,
    "status": git_status,
    "st": git_status,
    "add all": git_add_all,
    "add": git_add,
    "indir": indir,
    "y": y,
    "yükle": y,    
    "gitk": gitk,
    "k": gitk,
    "sh": git_show,
    "git show": git_show,
    "git diff": git_diff,
    "diff": git_diff,
    "rm": git_rm,
    "rmc": git_rm_cached,
    ".gitignore": gitignore,
    "gi": gitignore,
    "cam": commit_amend_m,
    "logn": git_log_args,
    "diffw": diff_commitID,
    "rev": git_revert,
    "res": git_resetHARD,
    "br -c": branch_create,
    "ch": git_checkout,
    "br -ch": checkout_b,
    "ch -d": checkout_d,
    "stash": git_stash,
    "stash -l": git_stash_list,
    "stash -p": git_stash_pop,
    "stash -c": git_stash_clear,
    "stash -a": git_stash_apply,
    "branch show":git_branch_show,
    "br -sh": git_branch_show,
    "mr -sq": git_merge_squash,
    "mr": git_merge,
    "mr -ab": git_merge_abort,
    "rebase": git_rebase,
    "rf": git_reflog,
    "mv": git_mv,
    "lf": git_log_follow,
    "bl": git_blame,
    "tag": git_tag,
    "tagln":git_tag_ln,
    "tagm":git_tag_message,
    "save": git_archive_output,
    "wd": wpdW_control,
    "wd return": wdReturn,
    "wd update": wdUpdateRom,
    "settings.xml": settings,
    "gl": git_pull,
    "gl -a": gitpull_Args,
    "gitp": git_push,
    "gitp -o -m": gitPush_oM,
    "gitp -a": gitPush_Args,
    "gitr": gitRemote,
    "gitr -v": gitRemoteV,
    #SC
    "dir": workplace_dir,
    "d": workplace_dir,
    "ls": workplace_dir,
    "dosya oluştur": dosyaolustur,
    "mk": dosyaolustur,
    "do": dosyaolustur,
    "clear": clear,
    "cls": clear,
    "sil": clear,
    "cd": cd,
    "copy": copy,
    "cp": copy,
    #AUTH
    "producer": producer,
    "author": producer,
    "by maker": producer
    }
def switch(case):
    return komutlar.get(case, default)()
while True:
    title = lambda: os.system("title Git Easy To Use by Burak Y. V3.1")
    title()
    komut = input("~#")
    print(switch(komut))
