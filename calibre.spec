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
Version:	0.7.29
Release:	2
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	%{name}-%{version}-nofonts.tar.bz2
# Source0-md5:	788c6435ed624e1538000880b923ef13
Source1:	generate-tarball.sh
Patch0:		%{name}-prefix.patch
Patch1:		%{name}-manpages.patch
Patch2:		%{name}-no-update.patch
Patch3:		%{name}-env_module.patch
Patch4:		%{name}-locales.patch
Patch5:		%{name}-mounthelper.patch
URL:		http://www.calibre-ebook.com/
BuildRequires:	ImageMagick-devel >= 6.6.4.7
BuildRequires:	chmlib-devel
BuildRequires:	pkgconfig
BuildRequires:	podofo-devel
BuildRequires:	poppler-Qt-devel
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-PIL
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-cssutils >= 0.9.7b3
BuildRequires:	python-dateutil
BuildRequires:	python-lxml
BuildRequires:	python-mechanize
BuildRequires:	python-modules-sqlite
BuildRequires:	python-sip-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	xdg-utils
Requires:	ImageMagick-coder-jpeg
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
%patch5 -p1

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

rm -f $RPM_BUILD_ROOT%{_bindir}/%{name}-uninstall

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/%{name}.ar.qm
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/%{name}.cs.qm
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/%{name}.da.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/%{name}.de.qm
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/%{name}.es.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/%{name}.fr.qm
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/%{name}.he.qm
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/%{name}.hu.qm
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/%{name}.ja.qm
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/%{name}.pl.qm
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/%{name}.pt.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/%{name}.ru.qm
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/%{name}.sk.qm
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/%{name}.sl.qm
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/%{name}.sv.qm
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/%{name}.uk.qm
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.zh_CN.qm
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.zh_TW.qm
%{_libdir}/%{name}
%{_mandir}/man1/*.1*

%files -n bash-completion-calibre
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*
