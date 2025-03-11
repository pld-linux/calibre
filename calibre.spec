#
# TODO: - rewrite generate-tarball.sh script to provide locales.zip handling (if needed)
#	- make separate server package with init-scripts, etc...
#
# NOTE:
# Upstream packages contain some non-free fonts which we cannot redistribute,
# so when upgrading calibre we should download upstream tarball by hand from
# https://download.calibre-ebook.com/ and run generate-tarball.sh script
# included as SourceX.
#
Summary:	E-book converter and library management
Summary(pl.UTF-8):	Konwerter oraz biblioteka dla e-booków
Name:		calibre
Version:	6.23.0
Release:	4
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	%{name}-%{version}-nofonts.tar.xz
# Source0-md5:	e0a8b9d98f888d1996e3a594edf13cb5
Source1:	generate-tarball.sh
Source2:	%{name}-mount-helper
Patch0:		%{name}-prefix.patch
Patch1:		%{name}-locales.patch
Patch2:		shebang-python-fix.patch
Patch3:		desktop-integration.patch
Patch4:		%{name}-env_module.patch
Patch5:		icu75.patch
%define		baeutifulsoup_ver 3.0.5
%define		pil_ver 1.1.6
%define		pyqt6_ver 6.3.1
%define		apsw_ver 3.38.0
%define		cssselect_ver 0.7.1
%define		cssutils_ver 1:0.9.9
%define		dateutil_ver 1.4.1
%define		dns_ver 1.6.0
%define		lxml_ver 2.2.1
%define		mechanize_ver 0.1.11
%define		msgpack_ver 1.0.0
%define		netifaces_ver 0.8
%define		psutil_ver 0.6.1
URL:		https://calibre-ebook.com/
BuildRequires:	ImageMagick-devel >= 6.6.4.7
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6WebEngine-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	chmlib-devel >= 0.40
BuildRequires:	hunspell-devel
BuildRequires:	hyphen-devel
BuildRequires:	libicu-devel
BuildRequires:	libinput-devel
BuildRequires:	libmtp-devel >= 1.1.5
BuildRequires:	libwmf-devel >= 0.2.8
BuildRequires:	mtdev-devel
BuildRequires:	pkgconfig
BuildRequires:	podofo-devel >= 0.8.2
BuildRequires:	poppler-glib-devel >= 0.28.1
BuildRequires:	poppler-qt6-devel >= 0.28.1
BuildRequires:	python3-PyQt6-devel-tools >= %{pyqt6_ver}
BuildRequires:	python3-PyQt-builder
BuildRequires:	python3-PyQt6 >= %{pyqt6_ver}
BuildRequires:	python3-PyQt6-uic >= %{pyqt6_ver}
BuildRequires:	python3-PyQt6-WebEngine
BuildRequires:	python3-apsw >= %{apsw_ver}
BuildRequires:	python3-bs4 >= %{baeutifulsoup_ver}
BuildRequires:	python3-css_parser
BuildRequires:	python3-cssselect >= %{cssselect_ver}
BuildRequires:	python3-cssutils >= %{cssutils_ver}
BuildRequires:	python3-dateutil >= %{dateutil_ver}
BuildRequires:	python3-devel >= 1:2.7.1
BuildRequires:	python3-dns >= %{dns_ver}
#BuildRequires:	python3-genshi
BuildRequires:	python3-html5-parser
BuildRequires:	python3-jeepney
BuildRequires:	python3-lxml >= %{lxml_ver}
BuildRequires:	python3-mechanize >= %{mechanize_ver}
BuildRequires:	python3-msgpack >= %{msgpack_ver}
BuildRequires:	python3-netifaces >= %{netifaces_ver}
BuildRequires:	python3-pillow >= %{pil_ver}
BuildRequires:	python3-psutil >= %{psutil_ver}
BuildRequires:	python3-regex
BuildRequires:	qt6-build
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
BuildRequires:	sip6
BuildRequires:	sip-PyQt6 >= %{pyqt6_ver}
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	unzip
BuildRequires:	xdg-utils
BuildRequires:	xz >= 1:4.999.7
Requires:	Qt6Svg
Requires:	Qt6WebEngine
Requires:	python3-PyQt6 >= %{pyqt6_ver}
Requires:	python3-PyQt6-WebEngine
Requires:	python3-apsw >= %{apsw_ver}
Requires:	python3-bs4 >= %{baeutifulsoup_ver}
Requires:	python3-css_parser
Requires:	python3-cssselect >= %{cssselect_ver}
Requires:	python3-cssutils >= %{cssutils_ver}
Requires:	python3-dateutil >= %{dateutil_ver}
Requires:	python3-dns >= %{dns_ver}
#Requires:	python3-genshi
Requires:	python3-html5-parser
Requires:	python3-jeepney
Requires:	python3-lxml >= %{lxml_ver}
Requires:	python3-mechanize >= %{mechanize_ver}
Requires:	python3-msgpack >= %{msgpack_ver}
Requires:	python3-netifaces >= %{netifaces_ver}
Requires:	python3-pillow >= %{pil_ver}
Requires:	python3-psutil >= %{psutil_ver}
Requires:	python3-regex
Suggests:	ImageMagick-coder-jpeg
Suggests:	ImageMagick-coder-png
### FIXME: libunrar.so is needed for rar-packed files
Suggests:	libunrar-devel
Suggests:	poppler-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calibre is meant to be a complete e-library solution. It includes
library management, format conversion, news feeds to ebook conversion
as well as e-book reader sync features.

Calibre is primarily a ebook cataloging program. It manages your ebook
collection for you. It is designed around the concept of the logical
book, i.e. a single entry in the database that may correspond to
ebooks in several formats. It also supports conversion to and from a
dozen different ebook formats.

Supported input formats are: MOBI, LIT, PRC, EPUB, CHM, ODT, HTML,
CBR, CBZ, RTF, TXT, PDF and LRS.

%description -l pl.UTF-8
Calibre to bardzo dobry i darmowy program do czytania e-książek.

Calibre umożliwia zarówno czytanie e-książek jak i konwersję wielu
formatów do ich postaci. Program obsługuje następujące typy plików:
import: LRF, PDF, LIT, RTF, OPF, MOBI, PRC, EPUB, FB2, IMP, RB i HTML
eksport: Mobi, LRF i EPUB oraz do aplikacji iPhone-reader i Stanza.

Ten czytnik e-książek oferuje również pobieranie okładek, komiksów i
najnowszych wiadomości z serwisów poświęconym e-książkom. Twórcy
dołączyli również aplikację, którą użytkownik może wykorzystać jako
swój własny serwer darmowych książek.

%package -n bash-completion-calibre
Summary:	bash-completion for calibre
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla calibre
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion
BuildArch:	noarch

%description -n bash-completion-calibre
bash-completion for calibre.

%description -n bash-completion-calibre -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla calibre.

%package -n zsh-completion-calibre
Summary:	zsh-completion for calibre
Summary(pl.UTF-8):	uzupełnianie nazw dla calibre w powłoce zsh
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion
BuildArch:	noarch

%description -n zsh-completion-calibre
zsh-completion for calibre.

%description -n zsh-completion-calibre -l pl.UTF-8
Pakiet ten dostarcza uzupełnianie nazw dla calibre w powłoce zsh.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# 64bit target build fix
%{__sed} -i -e "s!'/usr/lib'!'%{_libdir}'!g" setup/build_environment.py

# upstream decides to store locale files in a single zip file but we prefer separate .mo
mkdir resources/localization/locales
unzip resources/localization/locales.zip -d resources/localization/locales
chmod 755 resources/localization/locales/*
rm -f resources/localization/locales.zip

%build
CC="%{__cc}" \
CXX=%{__cxx} \
OVERRIDE_CFLAGS="%{rpmcflags}" \
OVERRIDE_LDFLAGS="%{rpmldflags}" \
QMAKE="%{_bindir}/qmake-qt6" \
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
# create directories for xdg-utils
install -d $RPM_BUILD_ROOT%{_datadir}/{icons/hicolor,packages,mime/packages,desktop-directories} \
$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{zsh_compdir}}

export XDG_DATA_DIRS="$RPM_BUILD_ROOT%{_datadir}"
export XDG_UTILS_INSTALL_MODE="system"
export LIBPATH="%{_libdir}"
%{__python3} setup.py install \
	--no-compile \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--sharedir=%{_datadir}

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' \
	 -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
	$RPM_BUILD_ROOT%{_bindir}/* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}/devices/cli.py \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}/devices/mtp/unix/upstream/update.py

cp -p resources/images/library.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-gui.png
cp -p resources/images/viewer.png $RPM_BUILD_ROOT%{_pixmapsdir}/calibre-viewer.png

%py3_comp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py3_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/localization/locales $RPM_BUILD_ROOT%{_localedir}

# set proper filenames for locales (TODO: switch to patch if possible)
for file in $RPM_BUILD_ROOT%{_localedir}/*; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\).*:\1:')
	mkdir $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES
	%{__mv} $RPM_BUILD_ROOT%{_localedir}/$lang/*.mo \
		$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES
done;
for file in $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/messages.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	%{__mv} $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/messages.mo \
		$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/%{name}.mo
done;
for file in $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/iso639.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	%{__mv} $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/iso639.mo \
		$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/%{name}_iso639.mo
done;
for file in $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/iso3166.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	%{__mv} $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/iso3166.mo \
		$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/%{name}_iso3166.mo
done;

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{km_KH,km}
# duplicates of bn,sl
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{bn_BD,sl_SI}
# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{jv,ltg,uz@Latn}

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name} --all-name
for file in $RPM_BUILD_ROOT%{_localedir}/*/lcdata.calibre_msgpack; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/.*:\1:')
	echo $file | %{__sed} "s:$RPM_BUILD_ROOT\(.*\):%lang($lang) \1:" >>%{name}.lang
done;

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_mime_database
%update_icon_cache hicolor

%postun
if [ $1 -eq 0 ] ; then
	%update_desktop_database
	%update_mime_database
	%update_icon_cache hicolor
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog.txt COPYRIGHT README.md
%attr(755,root,root) %{_bindir}/calibre
%attr(755,root,root) %{_bindir}/calibre-complete
%attr(755,root,root) %{_bindir}/calibre-customize
%attr(755,root,root) %{_bindir}/calibre-debug
%attr(755,root,root) %{_bindir}/calibre-mount-helper
%attr(755,root,root) %{_bindir}/calibre-parallel
%attr(755,root,root) %{_bindir}/calibre-server
%attr(755,root,root) %{_bindir}/calibre-smtp
%attr(755,root,root) %{_bindir}/calibredb
%attr(755,root,root) %{_bindir}/ebook-convert
%attr(755,root,root) %{_bindir}/ebook-device
%attr(755,root,root) %{_bindir}/ebook-edit
%attr(755,root,root) %{_bindir}/ebook-meta
%attr(755,root,root) %{_bindir}/ebook-polish
%attr(755,root,root) %{_bindir}/ebook-viewer
%attr(755,root,root) %{_bindir}/fetch-ebook-metadata
%attr(755,root,root) %{_bindir}/lrf2lrs
%attr(755,root,root) %{_bindir}/lrfviewer
%attr(755,root,root) %{_bindir}/lrs2lrf
%attr(755,root,root) %{_bindir}/markdown-calibre
%attr(755,root,root) %{_bindir}/web2disk
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/calibre-ebook-edit.metainfo.xml
%{_datadir}/metainfo/calibre-ebook-viewer.metainfo.xml
%{_datadir}/metainfo/calibre-gui.metainfo.xml
%{_desktopdir}/calibre-ebook-edit.desktop
%{_desktopdir}/calibre-ebook-viewer.desktop
%{_desktopdir}/calibre-gui.desktop
%{_desktopdir}/calibre-lrfviewer.desktop
%{_iconsdir}/hicolor/*x*/apps/calibre-*.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-lrf.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kindle-application.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-mobi8-ebook.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-mobipocket-ebook.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-topaz-ebook.png
%{_iconsdir}/hicolor/*x*/mimetypes/gnome-mime-application-lrf.png
%{_iconsdir}/hicolor/*x*/mimetypes/gnome-mime-application-x-kindle-application.png
%{_iconsdir}/hicolor/*x*/mimetypes/gnome-mime-application-x-mobi8-ebook.png
%{_iconsdir}/hicolor/*x*/mimetypes/gnome-mime-application-x-mobipocket-ebook.png
%{_iconsdir}/hicolor/*x*/mimetypes/gnome-mime-application-x-topaz-ebook.png
%{_iconsdir}/hicolor/*x*/mimetypes/gnome-mime-text-lrs.png
%{_iconsdir}/hicolor/*x*/mimetypes/text-lrs.png
%{_datadir}/mime/packages/calibre-mimetypes.xml
%{_pixmapsdir}/calibre-gui.png
%{_pixmapsdir}/calibre-viewer.png

%files -n bash-completion-calibre
%defattr(644,root,root,755)
%{bash_compdir}/*

%files -n zsh-completion-calibre
%defattr(644,root,root,755)
%{zsh_compdir}/_calibre
