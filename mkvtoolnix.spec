# needed or qt5 test program wont compile
%define Werror_cflags %nil

Summary:	Matroska multimedia file utils

Name:		mkvtoolnix
Version:	24.0.0
Release:	1
Url:		https://mkvtoolnix.download/index.html
Source0:	https://mkvtoolnix.download/sources/%{name}-%{version}.tar.xz
License:	GPLv2+ and LGPLv2+
Group:		Video
BuildRequires:	bzip2-devel
BuildRequires:	libebml-devel >= 1.3.5
BuildRequires:	lzo-devel
BuildRequires:	libmatroska-devel >= 1.4.8
BuildRequires:	magic-devel
BuildRequires:	qt5-devel
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	boost-devel >= 1.49
BuildRequires:	ruby
BuildRequires:  rubygems
BuildRequires:	ruby-rake
# Upstream need it both for man-page (penguin).
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
# Optional - for building the translated man pages (penguin).
BuildRequires: po4a
BuildRequires: pkgconfig(libcmark)

%description
These tools allow information about (mkvinfo) or extraction
from (mkvdemux) or creation of (mkvmerge) or the splitting of
(mkvsplit) Matroska files. Matroska is a new multimedia file
format aiming to become THE new container format for the future. You
can find more information about it and its underlying technology, the
Extensible Binary Meta Language (EBML), at http://www.matroska.org/

%files -f %{name}.lang
%doc COPYING README*
%{_bindir}/*
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_datadir}/man/ca
%{_datadir}/man/de
%{_datadir}/man/es
%{_datadir}/man/ja
%{_datadir}/man/ko
%{_datadir}/man/nl
%{_datadir}/man/pl
%{_datadir}/man/uk
%{_datadir}/man/zh_CN
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
# Add workaround for bug in gcc 4.7.2_2012.07
# otherwise configure won't find lambda functions support
%setup_compile_flags
export CXXFLAGS=`echo $CXXFLAGS | sed s/-gdwarf-4//`
%configure \
	--enable-qt \
	--disable-wxwidgets
rake -j1

%install
rake DESTDIR=%{buildroot} install
%find_lang %{name}
