#
# TODO: - xdg stuff (put desktops and icons in proper place)
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
Version:	0.7.46
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	%{name}-%{version}-nofonts.tar.xz
# Source0-md5:	13e788f227fd9fadb2157a1ec72913a3
Source1:	generate-tarball.sh
Patch0:		%{name}-prefix.patch
Patch1:		%{name}-manpages.patch
Patch2:		%{name}-no-update.patch
Patch3:		%{name}-env_module.patch
Patch4:		%{name}-locales.patch
URL:		http://www.calibre-ebook.com/
BuildRequires:	ImageMagick-devel >= 6.6.4.7
BuildRequires:	chmlib-devel
BuildRequires:	libicu-devel
BuildRequires:	pkgconfig
BuildRequires:	podofo-devel
BuildRequires:	poppler-Qt-devel
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-PIL
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-cssutils >= 1:0.9.7
BuildRequires:	python-dateutil
BuildRequires:	python-lxml
BuildRequires:	python-mechanize
BuildRequires:	python-modules-sqlite
BuildRequires:	python-sip-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.586
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xdg-utils
BuildRequires:	xz >= 1:4.999.7
Requires:	ImageMagick-coder-jpeg
Requires:	ImageMagick-coder-png
Requires:	python-BeautifulSoup
Requires:	python-PIL
Requires:	python-cssutils
Requires:	python-dateutil
Requires:	python-lxml
Requires:	python-mechanize
Requires:	python-modules-sqlite
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

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--libdir="%{_libdir}"

# move manpages and locales to proper place
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/man $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/localization/locales $RPM_BUILD_ROOT%{_datadir}/locale

# set proper filenames for locales (TODO: switch to patch if possible)
for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/messages.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/messages.mo \
	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo
done;
for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/iso639.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/iso639.mo \
	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}_iso639.mo
done;
for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/qt.qm; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv $file $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.$lang.qm
done;

%{__rm} $RPM_BUILD_ROOT%{_bindir}/%{name}-uninstall

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog.yaml COPYRIGHT README
%attr(755,root,root) %{_bindir}/calibre
%attr(755,root,root) %{_bindir}/calibre-complete
%attr(755,root,root) %{_bindir}/calibre-customize
%attr(755,root,root) %{_bindir}/calibre-debug
%attr(755,root,root) %{_bindir}/calibre-parallel
%attr(755,root,root) %{_bindir}/calibre-server
%attr(755,root,root) %{_bindir}/calibre-smtp
%attr(755,root,root) %{_bindir}/calibredb
%attr(755,root,root) %{_bindir}/ebook-convert
%attr(755,root,root) %{_bindir}/ebook-device
%attr(755,root,root) %{_bindir}/ebook-meta
%attr(755,root,root) %{_bindir}/ebook-viewer
%attr(755,root,root) %{_bindir}/epub-fix
%attr(755,root,root) %{_bindir}/fetch-ebook-metadata
%attr(755,root,root) %{_bindir}/librarything
%attr(755,root,root) %{_bindir}/lrf2lrs
%attr(755,root,root) %{_bindir}/lrfviewer
%attr(755,root,root) %{_bindir}/lrs2lrf
%attr(755,root,root) %{_bindir}/markdown-calibre
%attr(755,root,root) %{_bindir}/pdfmanipulate
%attr(755,root,root) %{_bindir}/web2disk
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/*.1*

%files -n bash-completion-calibre
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*
