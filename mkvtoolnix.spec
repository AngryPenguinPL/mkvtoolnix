Summary:	Matroska multimedia file utils
Name:		mkvtoolnix
Version:	6.2.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Video
Url:		http://www.bunkus.org/videotools/mkvtoolnix/
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.xz

BuildRequires:	gcc-c++ >= 4.6.0
BuildRequires:	ruby
BuildRequires:	boost-devel >= 1.46
BuildRequires:	bzip2-devel
BuildRequires:	libebml-devel >= 1.3.0
BuildRequires:	liblzo-devel
BuildRequires:	libmatroska-devel >= 1.4.0
BuildRequires:	magic-devel
BuildRequires:	wxgtku-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(vorbis)

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
# Add workaround for bug in gcc 4.7.2_2012.07
# otherwise configure won't find lambda functions support
%setup_compile_flags
export CXXFLAGS=`echo $CXXFLAGS | %__sed s/-gdwarf-4//`

%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
./drake %{_smp_mflags}

%install
./drake install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc README TODO ChangeLog* COPYING
%{_bindir}/*
%{_datadir}/applications/mkvinfo.desktop
%{_datadir}/applications/mkvmergeGUI.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(uk) %{_mandir}/uk/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*

