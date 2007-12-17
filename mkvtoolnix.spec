%define name mkvtoolnix
%define version 2.1.0
%define release %mkrel 1
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary: Matroska multimedia file utils
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
Source1: matroska-48.png
Source2: matroska-32.png
Source3: matroska-16.png
URL: http://www.bunkus.org/videotools/mkvtoolnix/
License: GPL
Group: Video
BuildRequires: libvorbis-devel
BuildRequires: libmatroska-devel >= 0.8.1
BuildRequires: wxgtku-devel >= 2.6
BuildRequires: liblzo-devel
BuildRequires: libmagic-devel
BuildRequires: libbzip2-devel
BuildRequires: libflac-devel
BuildRequires: libpcre-devel
BuildRequires: libexpat-devel

%description
These tools allow information about (mkvinfo) or extraction
from (mkvdemux) or creation of (mkvmerge) or the splitting of
(mkvsplit) Matroska files. Matroska is a new multimedia file
format aiming to become THE new container format for the future. You
can find more information about it and its underlying technology, the
Extensible Binary Meta Language (EBML), at http://www.matroska.org/

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p %buildroot%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/mkvinfo -g" \
needs="X11" \
icon="matroska.png" \
section="Multimedia/Video" \
title="Matroska Info" \
longtitle="Shows information of Matroska video or audio files" xdg="true"
?package(%name): \
command="%_bindir/mmg" \
needs="X11" \
icon="matroska.png" \
section="Multimedia/Video" \
title="Mkvmerge GUI" \
longtitle="Create Matroska video or audio files" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-mkvinfo.desktop << EOF
[Desktop Entry]
Name=Matroska Info
Comment=Shows information of Matroska video or audio files
Exec=mkvinfo -g
Icon=matroska
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;AudioVideoEditing;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-mmg.desktop << EOF
[Desktop Entry]
Name=Mkvmerge GUI
Comment=Create Matroska video or audio files
Exec=mmg
Icon=matroska
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;AudioVideoEditing;
EOF

install -D -m 644 %SOURCE1 %buildroot%_liconsdir/matroska.png
install -D -m 644 %SOURCE2 %buildroot%_iconsdir/matroska.png
install -D -m 644 %SOURCE3 %buildroot%_miconsdir/matroska.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus 

%files
%defattr(-,root,root)
%doc README TODO ChangeLog* COPYING
%_bindir/*
%_datadir/%name
%_datadir/applications/mandriva-*
%_mandir/man1/*
%_liconsdir/matroska.png
%_iconsdir/matroska.png
%_miconsdir/matroska.png
%_menudir/%name


