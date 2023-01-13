import subprocess
from os.path import basename
import os
import getpass

# check for sudo -l
def run_sudo():


    print(f"Checking for SUDO Permissions\n")
    output = subprocess.run(["sudo", "-l"], capture_output=True, text=True)
    print(output.stdout)


run_sudo()


# check for users using passwd file
def passwd():


    print(f"checking for user information\n")
    output = subprocess.run(["cat","/etc/passwd"],capture_output=True, text=True)
    out = output.stdout.split("\n")
    users = [user for user in out if "/bin/bash" in user]
    if users:
        print('\n'.join(users))


passwd()


# check if passwd file is writable 
def passwd_Writable():

    print("\nchecking for writable passwd file\n")
    output = subprocess.run(["ls","-l","/etc/passwd"], capture_output=True, text=True)
    out = output.stdout.split("\n")
    writable = [w for w in out if "-rw-r--rw-" in w]
    if writable:
       print("passwd file is writable\n")


passwd_Writable()

# check for readable shadow file
def shadow_read():
    print("checking for readable shadow file\n")
    output = subprocess.run(["ls","-l","/etc/shadow"], capture_output=True, text=True)
    out = output.stdout.split("\n")
    read = [r for r in out if "-rw-r--r--" in r]
    if read:
       print(f"shadow file is readable\n{out}")

shadow_read()
#check for writable shadow file
def shadow_write():
    print("checking for writable shadow file\n")
    output = subprocess.run(["ls","-l","/etc/shadow"], capture_output=True, text=True)
    out = output.stdout.split("\n")
    writeable = [w for w in out if "-rw-r--rw-" in w]
    if writeable:
       print(f"shadow file is writable\n{out}")


shadow_write()

# check for SUID binaries
def SUID():


    print(f"Checking for SUID Binaries\n")
    output = subprocess.run(["find", "/", "-perm","-u=s", "-type", "f"], capture_output=True, text=True)
    suids = output.stdout.split("\n")
    excluded = ["fusermount","Xorg.wrap","polkit-agent-helper-1","chrome-sandbox","dbus-daemon-launch-helper","vmware-user-suid-wrapper","ssh-keysign","chfn", "chsh", "fusermount3", "gpasswd", "kismet", "mount", "newgrp", "ntfs-3g", "passwd", "pkexec", "su", "sudo", "umount","pppd"]
    binaries = [binary for binary in suids if basename(binary) not in excluded]
    if binaries:
        print('\n'.join(binaries))

    else:
        print("no abnormal suids present")


SUID()

# check for cronjobs
def Cronjobs():


    print(f"Now Checking for cronjobs\n")
    output = subprocess.run(["cat","/etc/crontab"],capture_output=True, text=True)
    out = output.stdout.split("\n")
    jobs = [line for line in out if "*/5 * * * *" in line or "* * * * *" in line]
    if jobs:
        print("looks like theirs some interesting cronjobs\n",'\n'.join(jobs))

    else:
        print("no cronjobs running every minute or 5 minutes")


Cronjobs()

# check for kernel version
def kernel():


    print(f"Now Checking kernel version\n")
    output = subprocess.run(["uname","-a"],capture_output=True, text=True)
    print(output.stdout)


kernel()

# check for .conf files
def conf():
    print("checking for config files")
    excluded_files = [":etc:apt:listchanges.conf","mke2fs.conf","ld.so.conf","libaudit.conf","e2scrub.conf","gai.conf","ca-certificates.conf","nftables.conf","deluser.conf","reportbug.conf","resolv.conf","kernel-img.conf","adduser.conf","logrotate.conf","ucf.conf","xattr.conf","host.conf","sudo.conf","usb_modeswitch.conf","debconf.conf","pam.conf","sudo_logsrvd.conf","nsswitch.conf","smi.conf","libao.conf","fuse.conf","rsyslog.conf","sysctl.conf","sensors3.conf","discover-modprobe.conf","cups-files.conf","cups-browsed.conf","cupsd.conf","snmp.conf","subscriptions.conf","alsoft.conf","avahi-daemon.conf","udev.conf","vgauth.conf","xautostart.conf","tools.conf","90atk-adaptor.conf","90qt-a11y.conf","Vendor.conf","PackageKit.conf","libc.conf","x86_64-linux-gnu.conf","fakeroot-x86_64-linux-gnu.conf","limits.conf","faillock.conf","pam_env.conf","sepermit.conf","access.conf","group.conf","time.conf","namespace.conf","udisks2.conf","90gs-cjk-resource-korea1.conf","90gs-cjk-resource-gb1.conf","90gs-cjk-resource-cns1.conf","90gs-cjk-resource-japan2.conf","90gs-cjk-resource-japan1.conf","90-javascript-alias.conf","90-javascript-alias.conf","ipp-usb.conf","semanage.conf","resolved.conf","journald.conf","system.conf","networkd.conf","user.conf","sleep.conf","timesyncd.conf","pstore.conf","logind.conf","wpa_supplicant.conf","org.opensuse.CupsPkHelper.Mechanism.conf","org.freedesktop.ModemManager1.conf","avahi-dbus.conf","pulseaudio-system.conf","com.redhat.NewPrinterNotification.conf","dnsmasq.conf","org.freedesktop.DisplayManager.conf","org.freedesktop.PackageKit.conf","com.redhat.PrinterDriversInstaller.conf","speechd.conf","espeak-mbrola-generic.conf","festival.conf","espeak.conf","cicero.conf","espeak-ng.conf","espeak-ng-mbrola-generic.conf","ivona.conf","swift-generic.conf","flite.conf","llia_phon-generic.conf","mary-generic-disabled.conf","dtk-generic.conf","epos-generic.conf","emacs.conf","NetworkManager.conf","modules.conf","cups-filters.conf","fonts.conf","58-dejavu-lgc-serif.conf","20-unhint-small-dejavu-lgc-serif.conf","20-unhint-small-dejavu-lgc-sans-mono.conf","20-unhint-small-dejavu-lgc-sans.conf","57-dejavu-sans.conf","57-dejavu-sans-mono.conf","57-dejavu-serif.conf","30-droid-noto-mono.conf","20-unhint-small-dejavu-sans.conf","58-dejavu-lgc-sans-mono.conf","20-unhint-small-dejavu-sans-mono.conf","58-dejavu-lgc-sans.conf","20-unhint-small-dejavu-serif.conf","65-droid-sans-fallback.conf","65-fonts-persian.conf","58-dejavu-lgc-serif.conf","61-urw-nimbus-roman.conf","20-unhint-small-dejavu-lgc-serif.conf","49-sansserif.conf","10-scale-bitmap-fonts.conf","61-urw-nimbus-mono-ps.conf","61-urw-z003.conf","20-unhint-small-vera.conf","61-urw-standard-symbols-ps.conf","20-unhint-small-dejavu-lgc-sans-mono.conf","61-urw-d050000l.conf","45-latin.conf","20-unhint-small-dejavu-lgc-sans.conf","61-urw-fallback-backwards.conf","57-dejavu-sans.conf","45-generic.conf","57-dejavu-sans-mono.conf","65-nonlatin.conf","61-urw-fallback-generics.conf","57-dejavu-serif.conf","90-synthetic.conf","69-unifont.conf","61-urw-bookman.conf","60-generic.conf","60-latin.conf","20-unhint-small-dejavu-sans.conf","58-dejavu-lgc-sans-mono.conf","10-hinting-slight.conf","50-user.conf","61-urw-c059.conf","30-opensymbol.conf","20-unhint-small-dejavu-sans-mono.conf","61-urw-nimbus-sans.conf","58-dejavu-lgc-sans.conf","40-nonlatin.conf","20-unhint-small-dejavu-serif.conf","61-urw-gothic.conf","61-urw-p052.conf","11-lcdfilter-default.conf","51-local.conf","80-delicious.conf","30-metric-aliases.conf","70-no-bitmaps.conf","daemon.conf","client.conf","01-enable-autospawn.conf","hp4200.conf","epson.conf","ma1509.conf","matsushita.conf","epson2.conf","sm3840.conf","dell1600n_net.conf","coolscan.conf","kvs1025.conf","test.conf","coolscan3.conf","agfafocus.conf","dc210.conf","snapscan.conf","canon_pp.conf","umax.conf","u12.conf","apple.conf","hp5400.conf","plustek_pp.conf","pieusb.conf","s9036.conf","genesys.conf","gt68xx.conf","pixma.conf","dc240.conf","mustek_pp.conf","epjitsu.conf","sceptre.conf","umax_pp.conf","canon_lide70.conf","kodakaio.conf","magicolor.conf","epsonds.conf","dmc.conf","canon.conf","ibm.conf","mustek.conf","bh.conf","escl.conf","hs2p.conf","rts8891.conf","kodak.conf","nec.conf","net.conf","stv680.conf","artec_eplus48u.conf","gphoto2.conf","saned.conf","coolscan2.conf","mustek_usb.conf","hp.conf","teco2.conf","sp15c.conf","abaton.conf","artec.conf","canon630u.conf","avision.conf","teco1.conf","dc25.conf","microtek2.conf","sharp.conf","lexmark.conf","leo.conf","fujitsu.conf","cardscan.conf","xerox_mfp.conf","plustek.conf","teco3.conf","hp3900.conf","pie.conf","st400.conf","canon_dr.conf","tamarack.conf","hpsj5s.conf","ricoh.conf","dll.conf","microtek.conf","p5.conf","qcam.conf","umax1220u.conf","ports.conf","apache2.conf","autoindex.conf","dir.conf","alias.conf","reqtimeout.conf","mime.conf","setenvif.conf","mpm_event.conf","status.conf","deflate.conf","negotiation.conf","localized-error-pages.conf","other-vhosts-access-log.conf","serve-cgi-bin.conf","charset.conf","security.conf","000-default.conf","000-default.conf","default-ssl.conf","javascript-common.conf","localized-error-pages.conf","other-vhosts-access-log.conf","serve-cgi-bin.conf","charset.conf","security.conf","cgid.conf","mime_magic.conf","proxy_html.conf","mpm_prefork.conf","autoindex.conf","dir.conf","alias.conf","reqtimeout.conf","userdir.conf","mime.conf","setenvif.conf","info.conf","proxy_ftp.conf","actions.conf","proxy_balancer.conf","mpm_event.conf","ldap.conf","ssl.conf","status.conf","cache_disk.conf","deflate.conf","http2.conf","dav_fs.conf","mpm_worker.conf","proxy.conf","negotiation.conf","dhclient.conf","ldap.conf","50-oss.conf","99-pulse.conf","50-pulseaudio.conf","10-rate-lav.conf","10-samplerate.conf","60-upmix.conf","10-speexrate.conf","50-arcam-av-ctl.conf","60-vdownmix.conf","98-usb-stream.conf","50-jack.conf","60-a52-encoder.conf","listchanges.conf","parser.conf","snmp.conf","UPower.conf","im-multipress.conf","psprint.conf","plymouthd.conf","50-localauthority.conf","51-debian-sudo.conf","user-dirs.conf","pipewire.conf","alsa-monitor.conf","media-session.conf","keys.conf","lightdm.conf","users.conf","lightdm-gtk-greeter.conf","initramfs.conf","update-initramfs.conf","99-sysctl.conf","im-multipress.conf","99-environment.conf","resolv.conf","debian.conf","locale-gen.conf","10-defaults.conf","desktop.conf","defaults.conf","speech-dispatcher.conf","passwd.conf","systemd-pstore.conf","static-nodes-permissions.conf","home.conf","journal-nocow.conf","systemd.conf","dbus.conf","colord.conf","man-db.conf","systemd-tmp.conf","gvfsd-fuse-tmpfiles.conf","sudo.conf","x11.conf","open-vm-tools-desktop.conf","var.conf","debian.conf","systemd-nologin.conf","legacy.conf","tmp.conf","no-mac-addr-change.conf","open-vm-tools-desktop.conf","default.conf","systemd.conf","aliases.conf","fbdev-blacklist.conf","systemd.conf","dbus.conf","basic.conf","psprint.conf","protect-links.conf","50-bubblewrap.conf","50-pid-max.conf","analog-input-internal-mic-always.conf","analog-input-headset-mic.conf","hdmi-output-1.conf","iec958-stereo-output.conf","analog-input-mic-line.conf","analog-input-tvtuner.conf","hdmi-output-0.conf","analog-input.conf","hdmi-output-3.conf","hdmi-output-7.conf","hdmi-output-6.conf","usb-gaming-headset-output-stereo.conf","analog-output.conf","analog-output-speaker-always.conf","analog-input-mic.conf","hdmi-output-2.conf","analog-output-mono.conf","hdmi-output-4.conf","usb-gaming-headset-input.conf","analog-input-fm.conf","iec958-stereo-input.conf","analog-input-front-mic.conf","analog-output-headphones-2.conf","analog-output-headphones.conf","analog-input-aux.conf","hdmi-output-5.conf","analog-output-chat.conf","analog-input-headphone-mic.conf","analog-input-dock-mic.conf","analog-output-speaker.conf","virtual-surround-7.1.conf","analog-input-internal-mic.conf","usb-gaming-headset-output-mono.conf","analog-input-linein.conf","analog-input-video.conf","steelseries-arctis-output-chat-common.conf","analog-output-lineout.conf","steelseries-arctis-output-game-common.conf","analog-input-rear-mic.conf","usb-gaming-headset.conf","native-instruments-audio8dj.conf","native-instruments-korecontroller.conf","force-speaker.conf","native-instruments-traktorkontrol-s4.conf","sb-omni-surround-5.1.conf","default.conf","sennheiser-gsx.conf","cmedia-high-speed-true-hdaudio.conf","native-instruments-traktor-audio6.conf","behringer-umc22.conf","dell-dock-tb16-usb-audio.conf","kinect-audio.conf","steelseries-arctis-common-usb-audio.conf","native-instruments-traktor-audio10.conf","simple-headphones-mic.conf","hp-tbt-dock-audio-module.conf","native-instruments-traktor-audio2.conf","force-speaker-and-int-mic.conf","maudio-fasttrack-pro.conf","audigy.conf","hp-tbt-dock-120w-g2.conf","native-instruments-audio4dj.conf","adduser.conf","theme.conf","nsswitch.conf","65-fonts-persian.conf","10-no-sub-pixel.conf","49-sansserif.conf","10-scale-bitmap-fonts.conf","20-unhint-small-vera.conf","urw-gothic.conf","10-sub-pixel-bgr.conf","10-hinting-medium.conf","10-hinting-none.conf","45-latin.conf","25-unhint-nonlatin.conf","70-force-bitmaps.conf","urw-z003.conf","10-unhinted.conf","45-generic.conf","65-nonlatin.conf","urw-fallback-generics.conf","urw-p052.conf","10-sub-pixel-vrgb.conf","90-synthetic.conf","69-unifont.conf","urw-c059.conf","60-generic.conf","10-sub-pixel-vbgr.conf","60-latin.conf","65-khmer.conf","10-hinting-slight.conf","10-sub-pixel-rgb.conf","urw-nimbus-mono-ps.conf","urw-nimbus-roman.conf","70-yes-bitmaps.conf","50-user.conf","urw-standard-symbols-ps.conf","urw-bookman.conf","urw-d050000l.conf","urw-nimbus-sans.conf","30-opensymbol.conf","11-lcdfilter-legacy.conf","40-nonlatin.conf","10-hinting-full.conf","urw-fallback-specifics.conf","10-autohint.conf","urw-fallback-backwards.conf","11-lcdfilter-default.conf","51-local.conf","11-lcdfilter-light.conf","80-delicious.conf","30-metric-aliases.conf","70-no-bitmaps.conf","HP.conf","blacklist.conf","default.conf","debconf.conf","system.conf","session.conf","org.freedesktop.NetworkManager.conf","org.freedesktop.systemd1.conf","org.freedesktop.UDisks2.conf","org.freedesktop.timesync1.conf","org.freedesktop.locale1.conf","org.freedesktop.ColorManager.conf","org.freedesktop.resolve1.conf","org.freedesktop.PolicyKit1.conf","org.freedesktop.UPower.conf","org.freedesktop.RealtimeKit1.conf","org.freedesktop.login1.conf","org.freedesktop.timedate1.conf","org.freedesktop.network1.conf","nm-dispatcher.conf","org.freedesktop.hostname1.conf","speechd.conf","festival.conf","espeak.conf","cicero.conf","espeak-ng.conf","emacs.conf","trust-anchors.conf","analog-input-internal-mic-always.conf","analog-input-headset-mic.conf","hdmi-output-1.conf","iec958-stereo-output.conf","analog-input-mic-line.conf","analog-input-tvtuner.conf","hdmi-output-0.conf","analog-input.conf","hdmi-output-3.conf","hdmi-output-7.conf","hdmi-output-6.conf","usb-gaming-headset-output-stereo.conf","analog-output.conf","analog-output-speaker-always.conf","analog-input-mic.conf","hdmi-output-2.conf","analog-output-mono.conf","hdmi-output-4.conf","usb-gaming-headset-input.conf","analog-input-fm.conf","iec958-stereo-input.conf","analog-input-front-mic.conf","analog-output-headphones-2.conf","analog-output-headphones.conf","analog-input-aux.conf","hdmi-output-5.conf","analog-input-headphone-mic.conf","analog-input-dock-mic.conf","analog-output-speaker.conf","analog-input-internal-mic.conf","usb-gaming-headset-output-mono.conf","analog-input-linein.conf","analog-input-video.conf","steelseries-arctis-output-chat-common.conf","analog-output-lineout.conf","steelseries-arctis-output-game-common.conf","analog-input-rear-mic.conf","usb-gaming-headset.conf","native-instruments-audio8dj.conf","native-instruments-korecontroller.conf","force-speaker.conf","native-instruments-traktorkontrol-s4.conf","sb-omni-surround-5.1.conf","default.conf","cmedia-high-speed-true-hdaudio.conf","native-instruments-traktor-audio6.conf","dell-dock-tb16-usb-audio.conf","kinect-audio.conf","steelseries-arctis-common-usb-audio.conf","native-instruments-traktor-audio10.conf","native-instruments-traktor-audio2.conf","force-speaker-and-int-mic.conf","maudio-fasttrack-pro.conf","audigy.conf","native-instruments-audio4dj.conf","mm-foxconn-t77w968-carrier-mapping.conf","gpgconf.conf","adduser.local.conf","adduser.conf","tellerstats.conf","ftp-archive.conf","apt-ftparchive.conf","xorg.conf","sysctl.conf","apt.conf","gpgconf.conf","server.conf","cups-socket.public.conf","cups-socket.localhost.conf","client.conf","xconsole.conf","xconsole.conf","console.conf","req.conf","syslog.conf","sudo.conf","pam.conf","wpa_supplicant.conf","openCryptoki.conf","wpa-psk-tkip.conf","plaintext.conf","wep.conf","wpa-roam.conf","ieee8021x.conf","wpa2-eap-ccmp.conf","udhcpd-p2p.conf","alsa.conf","pulse-alsa.conf","ucm.conf","snd_soc_apq8016_sbc.conf","snd_soc_rockchip_max98090.conf","snd_soc_sdm845.conf","snd_soc_tegra_max98090.conf","snd_soc_rk3399_gru_sound.conf","snd_soc_snow.conf","snd_acp3x_rn.conf","snd_soc_omap_abe_twl6040.conf","snd_soc_tegra_alc5632.conf","snd_soc_apq8096.conf","linked.conf","snow.conf","HiFi.conf","HDA-Capture-value.conf","HDAudio-DualCodecs.conf","Hdmi.conf","HiFi-analog.conf","HiFi.conf","HiFi-dual.conf","HDAudio-Gigabyte-ALC1220DualCodecs.conf","HDA-Intel.conf","HDAudio-Lenovo-DualCodecs.conf","init.conf","HiFi-acp.conf","Hdmi.conf","rt1308-2.conf","rt1308-4.conf","rt715.conf","HiFi.conf","sof-soundwire.conf","rt700.conf","rt711.conf","rt5682.conf","max98090.conf","HiFi.conf","HiFi.conf","Record.conf","alc5632.conf","Lenovo-ThinkStation-P620-Rear-HiFi.conf","Lenovo-ThinkStation-P620-Main-HiFi.conf","Dell-WD15-Dock.conf","Lenovo-ThinkStation-P620-Rear.conf","Dell-WD15-Dock-HiFi.conf","Realtek-ALC1220-VB-Desktop.conf","Lenovo-ThinkStation-P620-Main.conf","Realtek-ALC1220-VB-Desktop-HiFi.conf","chtrt5650.conf","HiFi.conf","apq8096.conf","HDMI.conf","HiFi.conf","sdm845.conf","HDMI.conf","HiFi.conf","HDMI.conf","HiFi.conf","apq8016-sbc.conf","bytcht-es8316.conf","HiFi.conf","HiFi-LongName.conf","HiFi-Components.conf","Hdmi2.conf","hda-dsp.conf","HiFi.conf","Hdmi1.conf","HiFi.conf","bdw-rt5677.conf","skylake-rt286.conf","Hdmi2.conf","HiFi.conf","Hdmi1.conf","HiFi.conf","SOF.conf","abe-twl6040.conf","VoiceCall.conf","Voice.conf","HiFi.conf","Record.conf","FMAnalog.conf","SDP4430.conf","HiFiLP.conf","VoiceCall.conf","Pandaboard.conf","Voice.conf","HiFi.conf","Record.conf","FMAnalog.conf","HiFiLP.conf","PlatformEnableSeq.conf","PlatformDisableSeq.conf","Hdmi.conf","HiFi.conf","sof-hda-dsp.conf","Hdmi.conf","broxton-rt298.conf","HiFi.conf","bytcr-rt5651.conf","HiFi.conf","HiFi-LongName.conf","HiFi-Components.conf","HiFi.conf","bytcht-cx2072x.conf","HiFi.conf","rk3399-gru-sound.conf","max98090.conf","HiFi.conf","init.conf","SpeakerEnableSeq.conf","DigitalMicEnableSeq.conf","HeadphonesEnableSeq.conf","AnalogMic.conf","DisableSeq.conf","HSMicEnableSeq.conf","EnableSeq.conf","HSMicDisableSeq.conf","DigitalMicDisableSeq.conf","InternalMic.conf","MonoSpeaker.conf","HeadsetMic.conf","HeadPhones.conf","EnableSeq.conf","Speaker.conf","init.conf","MonoSpeaker.conf","IN1-InternalMic.conf","HeadPhones.conf","EnableSeq.conf","IN2-InternalMic.conf","IN2-HeadsetMic.conf","IN1-HeadsetMic.conf","Speaker.conf","MonoSpeaker.conf","DMIC2.conf","HeadsetMic.conf","HeadPhones.conf","EnableSeq.conf","DMIC1.conf","Speaker.conf","hdmi.conf","SpeakerEnableSeq.conf","SpeakerDisableSeq.conf","DefaultEnableSeq.conf","MonoSpeaker.conf","IN3-HeadsetMic.conf","IN1-InternalMic.conf","IN12-InternalMic.conf","HeadPhones.conf","EnableSeq.conf","IN2-InternalMic.conf","HeadPhones-swapped.conf","IN2-HeadsetMic.conf","DigitalMic.conf","Speaker.conf","DigitalMics.conf","MonoSpeaker.conf","IN1-InternalMic.conf","HeadsetMic.conf","HeadPhones.conf","EnableSeq.conf","IN3-InternalMic.conf","Speaker.conf","init.conf","InternalMic.conf","DisableSeq.conf","HeadsetMic.conf","HeadPhones.conf","EnableSeq.conf","Speaker.conf","Headphones.conf","InternalMic.conf","HeadsetMic.conf","EnableSeq.conf","Speaker.conf","HeadphoneEnableSeq.conf","SpeakerEnableSeq.conf","HeadphoneMicEnableSeq.conf","SpeakerDisableSeq.conf","HeadphoneDisableSeq.conf","HeadphoneMicDisableSeq.conf","DefaultEnableSeq.conf","DefaultDisableSeq.conf","init.conf","HiFi.conf","chtmax98090.conf","chtnau8824.conf","HiFi.conf","HiFi.conf","broadwell-rt286.conf","bytcr-rt5640.conf","HiFi.conf","HiFi-LongName.conf","HiFi-Components.conf","cht-bsw-rt5672.conf","HiFi.conf","Hdmi2.conf","HiFi.conf","kblrt5660.conf","Hdmi1.conf","HiFi.conf","chtrt5645.conf","50-oss.conf","pulse.conf","50-pulseaudio.conf","10-rate-lav.conf","10-samplerate.conf","60-upmix.conf","10-speexrate.conf","50-arcam-av-ctl.conf","60-vdownmix.conf","98-usb-stream.conf","50-jack.conf","60-a52-encoder.conf","Echo_Echo3G.conf","SI7018.conf","ICE1712.conf","CMI8738-MC8.conf","VIA8233.conf","RME9636.conf","ICH.conf","GUS.conf","RME9652.conf","AU8810.conf","PS3.conf","FM801.conf","ICE1724.conf","AU8820.conf","VIA8237.conf","Audigy2.conf","FWSpeakers.conf","ES1968.conf","VXPocket.conf","EMU10K1.conf","CS46xx.conf","CMI8788.conf","CA0106.conf","HdmiLpeAudio.conf","PMac.conf","YMF744.conf","CMI8338.conf","VIA8233A.conf","ICH-MODEM.conf","SB-XFi.conf","FireWave.conf","USB-Audio.conf","VXPocket440.conf","CMI8338-SWIEC.conf","Loopback.conf","NFORCE.conf","Audigy.conf","pistachio-card.conf","ICH4.conf","CMI8738-MC6.conf","ENS1371.conf","Aureon51.conf","EMU10K1X.conf","aliases.conf","ATIIXP.conf","ATIIXP-SPDMA.conf","HDA-Intel.conf","Maestro3.conf","ENS1370.conf","VX222.conf","Aureon71.conf","TRID4DWAVENX.conf","PC-Speaker.conf","AACI.conf","AU8830.conf","vc4-hdmi.conf","ATIIXP-MODEM.conf","PMacToonie.conf","VIA686A.conf","iec958.conf","surround50.conf","surround51.conf","surround41.conf","surround71.conf","dpl.conf","default.conf","hdmi.conf","center_lfe.conf","dmix.conf","modem.conf","dsnoop.conf","front.conf","rear.conf","surround40.conf","surround21.conf","side.conf","skl_hda_dsp_generic-tplg.conf","bxt_i2s.conf","broadwell.conf","skl_i2s.conf","accessibility.conf","fpdb.conf","00-mesa-defaults.conf","01_debian.conf","01_debian.conf","10-quirks.conf","10-amdgpu.conf","70-wacom.conf","10-radeon.conf","40-libinput.conf","resolv.conf","no-stub-resolv.conf","static-nodes.conf"]
    for root, dirs, files in os.walk('/'):
        for file in excluded_files:
            if file in files:
                files.remove(file)
        for file in files:
            if file.endswith('.conf'):
               os.access(file, os.W_OK) 
               print(file)
    

conf()


# check for directories owned by the current user 

def directories():
    print("checking for directories owned by our user")
    excluded_dirs = ["proc", "run", "user", "dev", "usr", "sys","etc",".cache",".config",".mozilla",".local",".ipython"]

    for root, dirs, files in os.walk('/'):
        for dir in excluded_dirs:
            if dir in dirs:
                dirs.remove(dir)
        for dir in dirs:
            full_path = os.path.join(root,dir)
            if os.stat(full_path).st_uid == os.getuid():
                print(full_path)
directories()

# get all files owned by root we can write to
def files():
    print("checking for files we can write to\n")
    excluded_dirs = ["proc", "run", "user", "dev", "usr", "sys","etc"]
    current_user = getpass.getuser() # get the current user
    for dirpath, dirnames, filenames in os.walk('/'): # for loop to get the dirs
        for directory in excluded_dirs: # remove the directories not wanted , starting here and finishing at next for loop
            if directory in dirnames:
                dirnames.remove(directory)
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if os.stat(full_path).st_uid == 0 and os.access(full_path, os.W_OK):
                print(f'{full_path} (file)')

files() 


# check for nfs no squash


server = input("Please enter the host ip: ")

def No_Squash(server):


    print(f"Cheching for possible nfs no squash")
    output = subprocess.run(["showmount", "-e", server], capture_output=True, text=True)
    out = output.stdout.decode()
    if "no_squash" in out:
        print(f"The nfs server {server} has no squash enabeled") 


No_Squash(server)
