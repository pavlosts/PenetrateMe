def find_port(port):

    portname = "N/A"
    vulns = "N/A"
    text = 'ports.txt'
    file = open(text, "a")

    if port == 21:
        portname = 'FTP'
        vulns = "List of some trojan horses/backdoors that also use this port: Back Construction, Blade Runner, " \
                "Cattivik FTP Server, CC Invader, Dark FTP, Doly Trojan, Fore, Invisible FTP, Juggernaut 42, Larva," \
                " MotIv FTP, Nerte 7.8.1, Net Administrator, Ramen, Senna Spy FTP server, The Flu, Traitor 21, WebEx," \
                " WinCrash, W32.Mytob.AE@mm, W32.Sober.N@mm."\
                " W32.Bobax.AF@mm (08.16.2005) - a mass-mailing worm that opens a backdoor and lowers security " \
                "settings on the compromised computer. It exploits the MS Plug and Play Buffer Overflow vulnerability "\
                "(MS Security Bulletin [MS05-039]) on port 21/tcp., and by sending copies of itself to gathered " \
                "email addresses. Also opens a backdoor on a random tcp port and/or port 80/udp." \
                "W32.Loxbot.C (01.11.2006)"

    elif port == 25:
        portname = 'SMTP'
        vulns = "SMTP (Simple Mail Transfer Protocol). Many worms contain their own SMTP engine and use it to " \
                "propagate by mass-mailing the payload, often also spoofing the \"From: ...\" field in emails. " \
                "If you are not running a mail server that you're aware of, there is a possibility your system " \
                "is infected. Integer overflow in Apple Safari [CVE-2010-1099], Arora [CVE-2010-1100], " \
                "Alexander Clauss iCab [CVE-2010-1101], OmniWeb [CVE-2010-1102], Stainless [CVE-2010-1103] allows " \
                "remote attackers to bypass intended port restrictions on outbound TCP connections via a port number " \
                "outside the range of the unsigned short data type, as demonstrated by a value of 65561 for TCP port 25." \
                "List of some trojan horses/backdoors that use this port: Ajan, Antigen, Barok, Email Password Sender " \
                "- EPS, EPS II, Gip, Gris, Happy99, Hpteam mail, Hybris, I love you, Kuang2, Magic Horse, MBT " \
                "(Mail Bombing Trojan), Moscow Email trojan, Naebi, NewApt worm, ProMail trojan, Shtirlitz, Stealth, " \
                "Tapiras, Terminator, WinPC, WinSpy W32.Sober.I@mm (11.19.2004) - mass-mailing worm that uses its own " \
                "SMTP engine. Affects all current Windows versions. Checks network connectivity by contacting a NTP " \
                "server on port 37/tcp. Trojan.Mitglieder.R (07.01.2005) - trojan with backdoor capabilities. " \
                "It runs a SOCKS4 proxy server and periodically contacts websites with information about the " \
                "compromised computer. Attempts to open a back door on port 9040/tcp. Might also initiate a SMTP " \
                "spam relay server on port 25/tcp. W32.Beagle.CX@mm (12.16.2005) - mass-mailing worm that uses " \
                "its own SMTP engine to spread Trojan.Lodear.E. Also opens a backdoor on port 80/tcp and lowers " \
                "security settings on the compromised computer. Backdoor.Rustock (01.12.2006) - backdoor program that " \
                "allows the compromised computer to be used as a proxy, uses rootkit techniques to hide its files and " \
                "registry entries."

    elif port == 26:
        portname = 'RSFTP'
        vulns = 'Port used by RSFTP - a simple FTP-like protocol.' \
                'Sometimes also used as an alternate to port 25 SMTP (Simple Mail Transfer Protocol).'

    elif port == 53:
        portname = 'DNS'
        vulns = 'DNS (Domain Name Service) is used for domain name resolution. Apple MacDNS, FaceTime also use this port.' \
                'There are some attacks that target vulnerabilities within DNS servers. Some trojans also use this port: ' \
                'ADM worm, li0n, MscanWorm, MuSka52, Trojan.Esteem.C (05.12.2005), W32.Spybot.ABDO (12.12.2005). ' \
                'W32.Dasher.B (12.16.2005) - a worm that exploits the MS Distributed Transaction Coordinator Remote ' \
                'exploit (MS Security Bulletin [MS05-051]). Listens for remote commands on port 53/tcp. Connects to an ' \
                'FTP server on port 21211/tcp. Scans for systems vulnerable to the [MS05-051] exploit on port 1025/tcp.'

    elif port == 80:
        portname = 'HTTP'
        vulns = "\t711 trojan (Seven Eleven), AckCmd, BlueFire, Cafeini, Duddie, Executor, God Message,\n" \
                "\tIntruzzo , Latinus, Lithium, MscanWorm, NerTe, Nimda, Noob, Optix Lite, Optix Pro , Power,\n" \
                "\tRamen, Remote Shell , Reverse WWW Tunnel Backdoor , RingZero, RTB 666, Scalper, Screen Cutter ,\n" \
                "\tSeeker, Slapper, Web Server CT , WebDownloader"

    elif port == 135:
        portname = "RPC"
        vulns = "\tThere is a RPC (a RPC's Endpoint Mapper component) vulnerability in Windows NT where a malformed\n" \
                "\trequest to port 135 could cause denial of service (DoS). RPC contains a flaw that causes it to\n" \
                "\tfail upon receipt of a request that contains a particular type of malformed data.\n\n" \
                "\tPort 135 is used by Messenger Service (not MSN Messenger) and exploited in popup net send\n" \
                "\tmessenger spam: MSKB 330904.\n\n" \
                "\tW32.Blaster.Worm is a widely spread worm that exploits the DCOM RPC vulnerability\n" \
                "\t(MS Security Bulletin [MS03-026]). The worm allows remote access to an infected computer\n" \
                "\tvia ports 4444/tcp and 69/UDP, and spreads through port 135/tcp.\n\n" \
                "\tW32.Reatle.E@mm (08.02.2005) - a mass-mailing worm that opens a backdoor and also spreads\n" \
                "\tby exploiting the MS DCOM RPC Vulnerability ([MS03-026]) on port 135/tcp. It uses its own\n" \
                "\tSMTP engine to email itself to gathered email addresses. Opens an FTP server on port 1155/tcp.\n" \
                "\tOpens a proxy server on port 2005/tcp. It also attempts to perform denial of service (DDoS) attack\n" \
                "\tagains known security websites on port 1052/tcp."

    elif port == 443:
        portname = "HTTPS"
        vulns = "\tSlapper trojan."

    elif port == 445:
        portname = "microsoft-ds"
        vulns = "\tLeaving port 445 open will leave you vulnerable to some worms, such as W32.Deloader and\n" \
                "\tIraqiWorm (aka Iraq_oil.exe ), W32.HLLW.Moega, W32.Sasser.Worm, W32.Korgo.AB (09.24.2004),\n" \
                "\tBackdoor.Rtkit.B (10.01.2004), Trojan.Netdepix.B (01.16.2005),\n" \
                "\tas well as the Windows Null Session Exploit."

    elif port == 554:
        portname = "ms-rtsp"
        vulns = "None found!"

    elif port == 902:
        portname = "902"
        vulns = "NetDevil - remote access trojan, 02.2002. Affects Windows 9x/Me/NT/2k/XP"

    elif port == 912:
        portname = "APEX"
        vulns = "TCP port 912 is vulnerable to multiple stack-based buffer overflows from specially crafted packets."

    file.write("Port : " + str(port) + "\n")
    file.write("Port name : " + portname + "\n")
    file.write("Known vulnerabilities:\n" + vulns)
    file.write("\n\n")

    file.close()
    return