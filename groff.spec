#
# Conditional build:
%bcond_without	xditview	# disable xditview (which requires X11)
#
Summary:	A document formatting system
Summary(de.UTF-8):	Ein Dokumentformatierungssystem
Summary(es.UTF-8):	Paquete groff GNU - formateador de texto
Summary(fr.UTF-8):	Paquetage de formatage de texte groff de GNU
Summary(pl.UTF-8):	GNU groff - pakiet do formatowania tekstu
Summary(pt_BR.UTF-8):	Pacote groff GNU - formatador de texto
Summary(ru.UTF-8):	GNU groff - пакет для форматирования текста
Summary(tr.UTF-8):	GNU groff metin biçemleme paketi
Summary(uk.UTF-8):	GNU groff - пакет для форматування тексту
Name:		groff
Version:	1.19.1
Release:	3
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.ffii.org/pub/groff/%{name}-%{version}.tar.gz
# Source0-md5:	57d155378640c12a80642664dfdfc892
Source1:	%{name}-trofftops.sh
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	3f8b22cc1eefb53306c8c2acf31aca29
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-colours.patch
Patch3:		%{name}-gcc4.patch
URL:		http://www.gnu.org/software/groff/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo >= 4.5
%if %{with xditview}
BuildRequires:	netpbm-progs
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-imake
%endif
Requires:	mktemp
Obsoletes:	groff-tools
Obsoletes:	groff-for-man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/share/X11/app-defaults

%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size,
bold type, italic type, the number and size of columns on a page, and
more. You should install groff if you want to use it as a document
formatting system. Groff can also be used to format man pages. If you
are going to use groff with the X Window System, you'll also need to
install the groff-gxditview package.

%description -l de.UTF-8
Groff ist ein Dokumentformatierungssystem. Groff liest Text und
Formatierungskommandos ein, und gibt formatierte Ausgabe aus. Die
erzeugten Dokumente können angezeigt oder ausgedruckt werden. Groffs
Formatierungsbefehle erlauben Ihnen, Schriftart und -größe, Fettdruck,
Kursivdruck, und die Anzahl der Spalten pro Seite usw. zu setzen. Sie
sollten groff installieren, wenn Sie es als
Dokumentformatierungssystem benutzen wollen. Groff ann auch benutzt
werden, um man-pages anzuziegen. Wenn Sie groff in X11 benutzen
wollten, brauchen Sie auch das groff-gxditview-Paket.

%description -l es.UTF-8
El sistema formateador de texto groff puede ser usado para crear
documentos con apariencia profesional tanto en papel como en la
pantalla. Todas las páginas de manuales son procesadas con groff,
entonces este paquete es necesario para leer estas páginas.

%description -l fr.UTF-8
Le système de formatage de texte groff peut être utilisé pour créer
des documents d'aspect professionnel sur papier et à l'écran. Toutes
les pages man sont traitées avec groff, vous avez donc besoin de ce
paquetage pour les visualiser.

%description -l pl.UTF-8
System formatowania tekstu groff może być używany do tworzenia
profesjonalnie wyglądającego dokumentu zarówno na papierze jak i na
konsoli. Wszystkie podręczniki ekranowe (man) potrzebują groff'a do
formatowania tekstu na ekranie. Tak więc potrzebujesz tego pakietu do
czytania podręczników ekranowych.

%description -l pt_BR.UTF-8
O sistema de formatação groff pode ser usado para criar documentos com
aparência profissional tanto em papel como na tela do computador.
Todas as páginas de manual on-line são processadas com groff, portanto
este pacote é necessário para ler estas páginas.

%description -l ru.UTF-8
Система форматирования текста groff может быть использована для
подготовки профессионально выглядящих документов как на бумаге, так и
на экране компьютера. Все man-страницы обрабатываются groff'ом, так
что без этого пакета вы не сможете их просматривать.

%description -l tr.UTF-8
groff metin biçemleme sistemi kağıt veya bilgisayar ekranı üzerinde
profesyonel görünüme sahip belgeler yaratmaya yarar. Bütün kılavuz
(man) sayfaları groff ile hazırlanmıştır. man sayfalarını okuyabilmek
için groff paketine gereksiniminiz olacaktır.

%description -l uk.UTF-8
Система форматування тексту groff може бути використана для підготовки
документів, що професійно виглядають як на папері, так і на екрані
комп'ютера. Всі man-сторінки обробляються groff'ом, так що без цього
пакету ви не зможете їх переглядати.

%package gxditview
Summary:	An X previewer for groff text processor output
Summary(de.UTF-8):	X-Anzeiger fuer groff Textprozessor-Ausgaben
Summary(es.UTF-8):	Groff GNU para X
Summary(fr.UTF-8):	Le visualiseur de fichier groff de GNU, sous X
Summary(pl.UTF-8):	Groff pod X
Summary(pt_BR.UTF-8):	Groff GNU para X
Summary(ru.UTF-8):	GNU gxditview - программа просмотра документов groff для X Window
Summary(tr.UTF-8):	GNU groff X görüntüleyici
Summary(uk.UTF-8):	GNU gxditview - програма перегляду документів groff для X Window
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXt >= 1.0.0

%description gxditview
Gxditview displays the groff text processor's output on an X Window
System display. If you are going to use groff as a text processor, you
should install gxditview so that you preview your processed text files
in X. You'll also need to install the groff package and the X Window
System.

%description gxditview -l de.UTF-8
Gxditview zeigt groff-Ausgaben auf einem X-Window-Display an. Wenn Sie
groff als Textprozessor benutzen wollen, und X11 benutzen, sollten Sie
gxditview installieren.

%description gxditview -l es.UTF-8
Este paquete contiene el programa gxditview, que se puede usar para
formatear y visualizar documentos en X window. Por ejemplo: páginas
man se las puede leer utilizando gxditview.

%description gxditview -l fr.UTF-8
Ce paquetage contient le programme gxditview, qui peut servir à
formater et viusaliser les documents groff sous X Window. Les pages
peuvent, par exemple, être lues avec gxditview.

%description gxditview -l pl.UTF-8
Pakiet ten zawiera program gxditview, który pozwoli Ci na formatowanie
dokumentów pod X. Na przykład, do czytania podręczników ekranowych.

%description gxditview -l pt_BR.UTF-8
Este pacote contém o programa gxditview, que pode ser usado para
formatar e visualizar documentos no X Window. Por exemplo: páginas man
podem ser lidas usando o gxditview.

%description gxditview -l ru.UTF-8
Этот пакет содержит программу gxditview, которая может быть
использована для форматирования и просмотра документов в формате groff
под X Window. Например, при помощи gxditview можно смотреть
man-страницы под X Window.

%description gxditview -l tr.UTF-8
Bu paket groff belgelerini görüntüleyip değiştirmeye yarayan gxditview
programını içerir. Örneğin man sayfaları gxditview kullanılarak
okunabilir.

%description gxditview -l uk.UTF-8
Цей пакет містить програму gxditview, яку можна використовувати для
форматування та перегляду документів у форматі groff під X Window.
Наприклад, за допомогою gxditview можна переглядати man-сторінки під X
Window.

%package perl
Summary:	Parts of the groff formatting system that require Perl
Summary(pl.UTF-8):	Cześć zasobów groff-a która wymaga Perla
Summary(ru.UTF-8):	Часть системы форматирования текста groff, требующая Perl
Summary(uk.UTF-8):	Частина системи форматування тексту groff, якій потрібен Perl
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description perl
groff-perl contains the parts of the groff text processor package that
require Perl. These include the afmtodit font processor used to create
PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the
troff-to-ps print filter.

%description perl -l pl.UTF-8
groff-perl zawiera część zasobów groff-a która wymaga Perla. Skrypt
afmtodit jest procesorem fontów używanym do tworzenia plików fontów w
formacie PostScript, a skrypt grok używany jest do automatycznego
doboru parametrów dla groff przy konwersji troff -> PostScript (zwykle
używany przy drukowaniu).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# makeinfo 4.7 has some problems when generating info without
# saving macro expanded file???
cd doc
makeinfo -E groff.texinfo2 groff.texinfo
mv -f groff.texinfo2 groff.texinfo

%build
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make} -j1

%if %{with xditview}
cd src/xditview
xmkmf
%{__make} -j1 \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/trofftops

%if %{with xditview}
%{__make} -j1 -C src/xditview install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	XAPPLOADDIR=%{_appdefsdir}
%endif

ln -sf s.tmac	$RPM_BUILD_ROOT%{_datadir}/groff/%{version}/tmac/gs.tmac
ln -sf mse.tmac	$RPM_BUILD_ROOT%{_datadir}/groff/%{version}/tmac/gmse.tmac
ln -sf m.tmac	$RPM_BUILD_ROOT%{_datadir}/groff/%{version}/tmac/gm.tmac
ln -sf eqn	$RPM_BUILD_ROOT%{_bindir}/geqn
ln -sf indxbib	$RPM_BUILD_ROOT%{_bindir}/gindxbib
ln -sf lookbib	$RPM_BUILD_ROOT%{_bindir}/glookbib
ln -sf neqn	$RPM_BUILD_ROOT%{_bindir}/gneqn
ln -sf nroff	$RPM_BUILD_ROOT%{_bindir}/gnroff
ln -sf troff	$RPM_BUILD_ROOT%{_bindir}/gtroff
ln -sf tbl	$RPM_BUILD_ROOT%{_bindir}/gtbl
ln -sf pic	$RPM_BUILD_ROOT%{_bindir}/gpic
ln -sf refer	$RPM_BUILD_ROOT%{_bindir}/grefer
ln -sf soelim	$RPM_BUILD_ROOT%{_bindir}/gsoelim

echo ".so eqn.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/geqn.1
echo ".so indxbib.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gindxbib.1
echo ".so lookbib.1" > $RPM_BUILD_ROOT%{_mandir}/man1/glookbib.1
echo ".so neqn.1" >    $RPM_BUILD_ROOT%{_mandir}/man1/gneqn.1
echo ".so nroff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gnroff.1
echo ".so pic.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gpic.1
echo ".so refer.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/grefer.1
echo ".so soelim.1" >  $RPM_BUILD_ROOT%{_mandir}/man1/gsoelim.1
echo ".so tbl.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gtbl.1
echo ".so troff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gtroff.1

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv -f $RPM_BUILD_ROOT%{_mandir}/ja/{man7/mmroff.7,man1/mmroff.1}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc BUG-REPORT ChangeLog NEWS PROBLEMS PROJECTS README TODO
%attr(755,root,root) %{_bindir}/addftinfo
%attr(755,root,root) %{_bindir}/eqn
%attr(755,root,root) %{_bindir}/eqn2graph
%attr(755,root,root) %{_bindir}/geqn
%attr(755,root,root) %{_bindir}/gindxbib
%attr(755,root,root) %{_bindir}/glookbib
%attr(755,root,root) %{_bindir}/gneqn
%attr(755,root,root) %{_bindir}/gnroff
%attr(755,root,root) %{_bindir}/gpic
%attr(755,root,root) %{_bindir}/grap2graph
%attr(755,root,root) %{_bindir}/grefer
%attr(755,root,root) %{_bindir}/grn
%attr(755,root,root) %{_bindir}/grodvi
%attr(755,root,root) %{_bindir}/groff
%attr(755,root,root) %{_bindir}/groffer
%attr(755,root,root) %{_bindir}/grolbp
%attr(755,root,root) %{_bindir}/grolj4
%attr(755,root,root) %{_bindir}/grops
%attr(755,root,root) %{_bindir}/grotty
%attr(755,root,root) %{_bindir}/gsoelim
%attr(755,root,root) %{_bindir}/gtbl
%attr(755,root,root) %{_bindir}/gtroff
%attr(755,root,root) %{_bindir}/hpftodit
%attr(755,root,root) %{_bindir}/indxbib
%attr(755,root,root) %{_bindir}/lkbib
%attr(755,root,root) %{_bindir}/lookbib
%attr(755,root,root) %{_bindir}/neqn
%attr(755,root,root) %{_bindir}/nroff
%attr(755,root,root) %{_bindir}/pfbtops
%attr(755,root,root) %{_bindir}/pic
%attr(755,root,root) %{_bindir}/pic2graph
%attr(755,root,root) %{_bindir}/post-grohtml
%attr(755,root,root) %{_bindir}/pre-grohtml
%attr(755,root,root) %{_bindir}/refer
%attr(755,root,root) %{_bindir}/soelim
%attr(755,root,root) %{_bindir}/tbl
%attr(755,root,root) %{_bindir}/tfmtodit
%attr(755,root,root) %{_bindir}/troff
%{_datadir}/groff
%{_mandir}/man1/addftinfo.1*
%{_mandir}/man1/eqn.1*
%{_mandir}/man1/eqn2graph.1*
%{_mandir}/man1/geqn.1*
%{_mandir}/man1/gindxbib.1*
%{_mandir}/man1/glookbib.1*
%{_mandir}/man1/gneqn.1*
%{_mandir}/man1/gnroff.1*
%{_mandir}/man1/gpic.1*
%{_mandir}/man1/grefer.1*
%{_mandir}/man1/grn.1*
%{_mandir}/man1/grodvi.1*
%{_mandir}/man1/groff.1*
%{_mandir}/man1/groffer.1*
%{_mandir}/man1/grohtml.1*
%{_mandir}/man1/grolbp.1*
%{_mandir}/man1/grolj4.1*
%{_mandir}/man1/grops.1*
%{_mandir}/man1/grotty.1*
%{_mandir}/man1/gsoelim.1*
%{_mandir}/man1/gtbl.1*
%{_mandir}/man1/gtroff.1*
%{_mandir}/man1/hpftodit.1*
%{_mandir}/man1/indxbib.1*
%{_mandir}/man1/lkbib.1*
%{_mandir}/man1/lookbib.1*
%{_mandir}/man1/neqn.1*
%{_mandir}/man1/nroff.1*
%{_mandir}/man1/pfbtops.1*
%{_mandir}/man1/pic.1*
%{_mandir}/man1/pic2graph.1*
%{_mandir}/man1/refer.1*
%{_mandir}/man1/soelim.1*
%{_mandir}/man1/tbl.1*
%{_mandir}/man1/tfmtodit.1*
%{_mandir}/man1/troff.1*
%{_mandir}/man5/*
%{_mandir}/man7/[!m]*

%lang(de) %{_mandir}/de/man1/groff.1*

%lang(fi) %{_mandir}/fi/man1/addftinfo.1*

%lang(ja) %{_mandir}/ja/man1/addftinfo.1*
%lang(ja) %{_mandir}/ja/man1/eqn.1*
%lang(ja) %{_mandir}/ja/man1/geqn.1*
%lang(ja) %{_mandir}/ja/man1/gindxbib.1*
%lang(ja) %{_mandir}/ja/man1/glookbib.1*
%lang(ja) %{_mandir}/ja/man1/gneqn.1*
%lang(ja) %{_mandir}/ja/man1/gnroff.1*
%lang(ja) %{_mandir}/ja/man1/gpic.1*
%lang(ja) %{_mandir}/ja/man1/grefer.1*
%lang(ja) %{_mandir}/ja/man1/grn.1*
%lang(ja) %{_mandir}/ja/man1/grodvi.1*
%lang(ja) %{_mandir}/ja/man1/groff.1*
%lang(ja) %{_mandir}/ja/man1/grohtml.1*
%lang(ja) %{_mandir}/ja/man1/grolbp.1*
%lang(ja) %{_mandir}/ja/man1/grolj4.1*
%lang(ja) %{_mandir}/ja/man1/grops.1*
%lang(ja) %{_mandir}/ja/man1/grotty.1*
%lang(ja) %{_mandir}/ja/man1/gsoelim.1*
%lang(ja) %{_mandir}/ja/man1/gtbl.1*
%lang(ja) %{_mandir}/ja/man1/gtroff.1*
%lang(ja) %{_mandir}/ja/man1/hpftodit.1*
%lang(ja) %{_mandir}/ja/man1/indxbib.1*
%lang(ja) %{_mandir}/ja/man1/lkbib.1*
%lang(ja) %{_mandir}/ja/man1/lookbib.1*
%lang(ja) %{_mandir}/ja/man1/nroff.1*
%lang(ja) %{_mandir}/ja/man1/pfbtops.1*
%lang(ja) %{_mandir}/ja/man1/pic.1*
%lang(ja) %{_mandir}/ja/man1/refer.1*
%lang(ja) %{_mandir}/ja/man1/soelim.1*
%lang(ja) %{_mandir}/ja/man1/tbl.1*
%lang(ja) %{_mandir}/ja/man1/tfmtodit.1*
%lang(ja) %{_mandir}/ja/man1/troff.1*
%lang(ja) %{_mandir}/ja/man5/*
%lang(ja) %{_mandir}/ja/man7/[!m]*

%lang(pl) %{_mandir}/pl/man1/gnroff.1*
%lang(pl) %{_mandir}/pl/man1/groff.1*
%lang(pl) %{_mandir}/pl/man1/gsoelim.1*
%lang(pl) %{_mandir}/pl/man1/gtbl.1*
%lang(pl) %{_mandir}/pl/man1/nroff.1*
%lang(pl) %{_mandir}/pl/man1/soelim.1*
%lang(pl) %{_mandir}/pl/man1/tbl.1*

%{_infodir}/*info*

%if %{with xditview}
%files gxditview
%defattr(644,root,root,755)
%doc src/xditview/{ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/gxditview
%{_appdefsdir}/GXditview
%{_mandir}/man1/*
%endif

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afmtodit
%attr(755,root,root) %{_bindir}/grog
%attr(755,root,root) %{_bindir}/mmroff
%attr(755,root,root) %{_bindir}/trofftops
%{_mandir}/man1/afmtodit.*
%{_mandir}/man1/grog.*
%{_mandir}/man1/mmroff.*

%lang(fi) %{_mandir}/fi/man1/afmtodit.*

%lang(ja) %{_mandir}/ja/man1/grog.*
%lang(ja) %{_mandir}/ja/man1/mmroff.*
