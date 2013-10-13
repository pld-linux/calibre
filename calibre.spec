#
# TODO: - rewrite generate-tarball.sh script to provide locales.zip handling (if needed)
#	- make separate server package with init-scripts, etc...
#	- -locales.patch needs love
#
# NOTE:
# Upstream packages some unfree fonts which we cannot redistribute,
# so when upgrading calibre we should download upstream tarball by hand from
# http://downloads.sourceforge.net/calibre and run generate-tarball.sh script
# included as SourceX.
#
Summary:	E-book converter and library management
Summary(pl.UTF-8):	Konwerter oraz biblioteka dla e-booków
Name:		calibre
Version:	1.6.0
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	%{name}-%{version}-nofonts.tar.xz
# Source0-md5:	817edf5bf3d54f53ead7c059c4937e1f
Source1:	generate-tarball.sh
Source2:	%{name}-mount-helper
Patch0:		%{name}-prefix.patch
Patch1:		%{name}-no-update.patch
Patch2:		%{name}-env_module.patch
Patch3:		%{name}-locales.patch
Patch4:		shebang-python-fix.patch
Patch5:		imagemagick-6.8.patch
Patch6:		qt4-private.patch
URL:		http://www.calibre-ebook.com/
%define		baeutifulsoup_ver 3.0.5
%define		pil_ver 1.1.6
%define		pyqt4_ver 4.9.1
%define		apsw_ver 3.8.0.1
%define		cssselect_ver 0.7.1
%define		cssutils_ver 1:0.9.9
%define		dateutil_ver 1.4.1
%define		dns_ver 1.6.0
%define		lxml_ver 2.2.1
%define		mechanize_ver 0.1.11
%define		netifaces_ver 0.8
%define		psutil_ver 0.6.1
BuildRequires:	ImageMagick-devel >= 6.6.4.7
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	chmlib-devel >= 0.40
BuildRequires:	libicu-devel
BuildRequires:	libmtp-devel >= 1.1.5
BuildRequires:	libwmf-devel >= 0.2.8
BuildRequires:	pkgconfig
BuildRequires:	podofo-devel >= 0.8.2
BuildRequires:	poppler-Qt-devel >= 0.20.2
BuildRequires:	poppler-glib-devel >= 0.20.2
BuildRequires:	python-BeautifulSoup >= %{baeutifulsoup_ver}
BuildRequires:	python-PIL >= %{pil_ver}
BuildRequires:	python-PyQt4 >= %{pyqt4_ver}
BuildRequires:	python-PyQt4-devel >= %{pyqt4_ver}
BuildRequires:	python-PyQt4-devel-tools >= %{pyqt4_ver}
BuildRequires:	python-apsw >= %{apsw_ver}
BuildRequires:	python-cssselect >= %{cssselect_ver}
BuildRequires:	python-cssutils >= %{cssutils_ver}
BuildRequires:	python-dateutil >= %{dateutil_ver}
BuildRequires:	python-devel >= 1:2.7.1
BuildRequires:	python-dns >= %{dns_ver}
BuildRequires:	python-genshi
BuildRequires:	python-lxml >= %{lxml_ver}
BuildRequires:	python-mechanize >= %{mechanize_ver}
BuildRequires:	python-modules-sqlite
BuildRequires:	python-netifaces >= %{netifaces_ver}
BuildRequires:	python-psutil >= %{psutil_ver}
BuildRequires:	python-sip-devel
BuildRequires:	qt4-devel-private
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.586
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	unzip
BuildRequires:	xdg-utils
BuildRequires:	xz >= 1:4.999.7
Requires:	python-BeautifulSoup >= %{baeutifulsoup_ver}
Requires:	python-PIL >= %{pil_ver}
Requires:	python-PyQt4 >= %{pyqt4_ver}
Requires:	python-apsw >= %{apsw_ver}
Requires:	python-cssselect >= %{cssselect_ver}
Requires:	python-cssutils >= %{cssutils_ver}
Requires:	python-dateutil >= %{dateutil_ver}
Requires:	python-dns >= %{dns_ver}
Requires:	python-genshi
Requires:	python-lxml >= %{lxml_ver}
Requires:	python-mechanize >= %{mechanize_ver}
Requires:	python-modules-sqlite
Requires:	python-netifaces >= %{netifaces_ver}
Requires:	python-psutil >= %{psutil_ver}
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

%description -n zsh-completion-calibre
zsh-completion for calibre.

%description -n zsh-completion-calibre -l pl.UTF-8
Pakiet ten dostarcza uzupełnianie nazw dla calibre w powłoce zsh.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
# create directories for xdg-utils
install -d $RPM_BUILD_ROOT%{_datadir}/{icons/hicolor,packages,mime/packages,desktop-directories} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/usr/share/zsh/site-functions}

XDG_DATA_DIRS="$RPM_BUILD_ROOT%{_datadir}" \
XDG_UTILS_INSTALL_MODE="system" \
LIBPATH="%{_libdir}" \
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--libdir="%{_libdir}"

cp -p resources/images/library.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-gui.png
cp -p resources/images/viewer.png $RPM_BUILD_ROOT%{_pixmapsdir}/calibre-viewer.png

%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_postclean %{_libdir}/%{name}

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/localization/locales $RPM_BUILD_ROOT%{_localedir}

# set proper filenames for locales (TODO: switch to patch if possible)
for file in $RPM_BUILD_ROOT%{_localedir}/*; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\).*:\1:')
	mkdir $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES
	mv $RPM_BUILD_ROOT%{_localedir}/$lang/*.mo \
	$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES
done;
for file in $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/messages.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/messages.mo \
	$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/%{name}.mo
done;
for file in $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/iso639.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/iso639.mo \
	$RPM_BUILD_ROOT%{_localedir}/$lang/LC_MESSAGES/%{name}_iso639.mo
done;

%{__rm} $RPM_BUILD_ROOT%{_bindir}/%{name}-uninstall

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ber
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/jv
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ltg
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/en_AU

install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name} --all-name

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
%doc Changelog.yaml COPYRIGHT README.md
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
%attr(755,root,root) %{_bindir}/ebook-meta
%attr(755,root,root) %{_bindir}/ebook-polish
%attr(755,root,root) %{_bindir}/ebook-viewer
%attr(755,root,root) %{_bindir}/fetch-ebook-metadata
%attr(755,root,root) %{_bindir}/lrf2lrs
%attr(755,root,root) %{_bindir}/lrfviewer
%attr(755,root,root) %{_bindir}/lrs2lrf
%attr(755,root,root) %{_bindir}/markdown-calibre
%attr(755,root,root) %{_bindir}/web2disk
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_desktopdir}/calibre-ebook-viewer.desktop
%{_desktopdir}/calibre-gui.desktop
%{_desktopdir}/calibre-lrfviewer.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/mime/application/*.xml
%{_datadir}/mime/text/*.xml
%{_datadir}/mime/packages/calibre-mimetypes.xml
%{_pixmapsdir}/%{name}-gui.png
%{_pixmapsdir}/calibre-viewer.png

%files -n bash-completion-calibre
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*

%files -n zsh-completion-calibre
%defattr(644,root,root,755)
%{_datadir}/zsh/site-functions/*
