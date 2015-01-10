def find_port(port):

    portname = "N/A"
    vulns = "N/A"
    text = 'ports.txt'
    file = open(text, "w")

    if port == 80:
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
        print("Inside if 443")
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