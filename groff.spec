#
# _without_xditview         - disable xditwiev
#

Summary:	A document formatting system
Summary(de):	Ein Dokumentformatierungssystem
Summary(es):	Paquete groff GNU - formateador de texto
Summary(fr):	Paquetage de formatage de texte groff de GNU
Summary(pl):	GNU groff - pakiet do formatowania tekstu
Summary(pt_BR):	Pacote groff GNU - formatador de texto
Summary(ru):	GNU groff - ÐÁËÅÔ ÄÌÑ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ ÔÅËÓÔÁ
Summary(tr):	GNU groff metin biçemleme paketi
Summary(uk):	GNU groff - ÐÁËÅÔ ÄÌÑ ÆÏÒÍÁÔÕ×ÁÎÎÑ ÔÅËÓÔÕ
Name:		groff
Version:	1.19
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.ffii.org/pub/groff/%{name}-%{version}.tar.gz
# Source0-md5: c12bf574120df33ec8c18d92703e099e
Source1:	%{name}-trofftops.sh
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5: 3f8b22cc1eefb53306c8c2acf31aca29
Patch0:		%{name}-safer.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-colours.patch
%{!?_without_xditview:BuildRequires:	XFree86-devel}
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
%{!?_without_xditview:BuildRequires:	netpbm-progs}
BuildRequires:	texinfo >= 4.5
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	groff-tools
Obsoletes:	groff-for-man

%define		_xprefix	/usr/X11R6
%define		_xbindir	%{_xprefix}/bin
%define		_xlibdir	%{_xprefix}/lib
%define		_xmandir	%{_xprefix}/man

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

%description -l de
Groff ist ein Dokumentformatierungssystem. Groff liest Text und
Formatierungskommandos ein, und gibt formatierte Ausgabe aus. Die
erzeugten Dokumente können angezeigt oder ausgedruckt werden. Groffs
Formatierungsbefehle erlauben Ihnen, Schriftart und -größe, Fettdruck,
Kursivdruck, und die Anzahl der Spalten pro Seite usw. zu setzen. Sie
sollten groff installieren, wenn Sie es als
Dokumentformatierungssystem benutzen wollen. Groff ann auch benutzt
werden, um man-pages anzuziegen. Wenn Sie groff in X11 benutzen
wollten, brauchen Sie auch das groff-gxditview-Paket.

%description -l es
El sistema formateador de texto groff puede ser usado para crear
documentos con apariencia profesional tanto en papel como en la
pantalla. Todas las páginas de manuales son procesadas con groff,
entonces este paquete es necesario para leer estas páginas.

%description -l fr
Le système de formatage de texte groff peut être utilisé pour créer
des documents d'aspect professionnel sur papier et à l'écran. Toutes
les pages man sont traitées avec groff, vous avez donc besoin de ce
paquetage pour les visualiser.

%description -l pl
System formatowania tekstu groff mo¿e byæ u¿ywany do tworzenia
profesjonalnie wygl±daj±cego dokumentu zarówno na papierze jak i na
konsoli. Wszystkie podrêczniki ekranowe (man) potrzebuj± groff'a do
formatowania tekstu na ekranie. Tak wiêc potrzebujesz tego pakietu do
czytania podrêczników ekranowych.

%description -l pt_BR
O sistema de formatação groff pode ser usado para criar documentos com
aparência profissional tanto em papel como na tela do computador.
Todas as páginas de manual on-line são processadas com groff, portanto
este pacote é necessário para ler estas páginas.

%description -l ru
óÉÓÔÅÍÁ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ ÔÅËÓÔÁ groff ÍÏÖÅÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎÁ ÄÌÑ
ÐÏÄÇÏÔÏ×ËÉ ÐÒÏÆÅÓÓÉÏÎÁÌØÎÏ ×ÙÇÌÑÄÑÝÉÈ ÄÏËÕÍÅÎÔÏ× ËÁË ÎÁ ÂÕÍÁÇÅ, ÔÁË É
ÎÁ ÜËÒÁÎÅ ËÏÍÐØÀÔÅÒÁ. ÷ÓÅ man-ÓÔÒÁÎÉÃÙ ÏÂÒÁÂÁÔÙ×ÁÀÔÓÑ groff'ÏÍ, ÔÁË
ÞÔÏ ÂÅÚ ÜÔÏÇÏ ÐÁËÅÔÁ ×Ù ÎÅ ÓÍÏÖÅÔÅ ÉÈ ÐÒÏÓÍÁÔÒÉ×ÁÔØ.

%description -l tr
groff metin biçemleme sistemi kaðýt veya bilgisayar ekraný üzerinde
profesyonel görünüme sahip belgeler yaratmaya yarar. Bütün kýlavuz
(man) sayfalarý groff ile hazýrlanmýþtýr. man sayfalarýný okuyabilmek
için groff paketine gereksiniminiz olacaktýr.

%description -l uk
óÉÓÔÅÍÁ ÆÏÒÍÁÔÕ×ÁÎÎÑ ÔÅËÓÔÕ groff ÍÏÖÅ ÂÕÔÉ ×ÉËÏÒÉÓÔÁÎÁ ÄÌÑ Ð¦ÄÇÏÔÏ×ËÉ
ÄÏËÕÍÅÎÔ¦×, ÝÏ ÐÒÏÆÅÓ¦ÊÎÏ ×ÉÇÌÑÄÁÀÔØ ÑË ÎÁ ÐÁÐÅÒ¦, ÔÁË ¦ ÎÁ ÅËÒÁÎ¦
ËÏÍÐ'ÀÔÅÒÁ. ÷Ó¦ man-ÓÔÏÒ¦ÎËÉ ÏÂÒÏÂÌÑÀÔØÓÑ groff'ÏÍ, ÔÁË ÝÏ ÂÅÚ ÃØÏÇÏ
ÐÁËÅÔÕ ×É ÎÅ ÚÍÏÖÅÔÅ §È ÐÅÒÅÇÌÑÄÁÔÉ.

%package gxditview
Summary:	An X previewer for groff text processor output
Summary(de):	X-Anzeiger fuer groff Textprozessor-Ausgaben
Summary(es):	Groff GNU para X
Summary(fr):	Le visualiseur de fichier groff de GNU, sous X
Summary(pl):	Groff pod X
Summary(pt_BR):	Groff GNU para X
Summary(ru):	GNU gxditview - ÐÒÏÇÒÁÍÍÁ ÐÒÏÓÍÏÔÒÁ ÄÏËÕÍÅÎÔÏ× groff ÄÌÑ X Window
Summary(tr):	GNU groff X görüntüleyici
Summary(uk):	GNU gxditview - ÐÒÏÇÒÁÍÁ ÐÅÒÅÇÌÑÄÕ ÄÏËÕÍÅÎÔ¦× groff ÄÌÑ X Window
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description gxditview
Gxditview displays the groff text processor's output on an X Window
System display. If you are going to use groff as a text processor, you
should install gxditview so that you preview your processed text files
in X. You'll also need to install the groff package and the X Window
System.

%description gxditview -l de
Gxditview zeigt groff-Ausgaben auf einem X-Window-Display an. Wenn Sie
groff als Textprozessor benutzen wollen, und X11 benutzen, sollten Sie
gxditview installieren.

%description gxditview -l es
Este paquete contiene el programa gxditview, que se puede usar para
formatear y visualizar documentos en X window. Por ejemplo: páginas
man se las puede leer utilizando gxditview.

%description gxditview -l fr
Ce paquetage contient le programme gxditview, qui peut servir à
formater et viusaliser les documents groff sous X Window. Les pages
peuvent, par exemple, être lues avec gxditview.

%description gxditview -l pl
Pakiet ten zawiera program gxditview, który pozwoli Ci na formatowanie
dokumentów pod X. Na przyk³ad, do czytania porêczników ekranowych.

%description gxditview -l pt_BR
Este pacote contém o programa gxditview, que pode ser usado para
formatar e visualizar documentos no X Window. Por exemplo: páginas man
podem ser lidas usando o gxditview.

%description gxditview -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÐÒÏÇÒÁÍÍÕ gxditview, ËÏÔÏÒÁÑ ÍÏÖÅÔ ÂÙÔØ
ÉÓÐÏÌØÚÏ×ÁÎÁ ÄÌÑ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ É ÐÒÏÓÍÏÔÒÁ ÄÏËÕÍÅÎÔÏ× × ÆÏÒÍÁÔÅ groff
ÐÏÄ X Window. îÁÐÒÉÍÅÒ, ÐÒÉ ÐÏÍÏÝÉ gxditview ÍÏÖÎÏ ÓÍÏÔÒÅÔØ
man-ÓÔÒÁÎÉÃÙ ÐÏÄ X Window.

%description gxditview -l tr
Bu paket groff belgelerini görüntüleyip deðiþtirmeye yarayan gxditview
programýný içerir. Örneðin man sayfalarý gxditview kullanýlarak
okunabilir.

%description gxditview -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÐÒÏÇÒÁÍÕ gxditview, ÑËÕ ÍÏÖÎÁ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ ÄÌÑ
ÆÏÒÍÁÔÕ×ÁÎÎÑ ÔÁ ÐÅÒÅÇÌÑÄÕ ÄÏËÕÍÅÎÔ¦× Õ ÆÏÒÍÁÔ¦ groff Ð¦Ä X Window.
îÁÐÒÉËÌÁÄ, ÚÁ ÄÏÐÏÍÏÇÏÀ gxditview ÍÏÖÎÁ ÐÅÒÅÇÌÑÄÁÔÉ man-ÓÔÏÒ¦ÎËÉ Ð¦Ä X
Window.

%package perl
Summary:	Parts of the groff formatting system that require Perl
Summary(pl):	Cze¶æ zasobów groff-a która wymaga Perla
Summary(ru):	þÁÓÔØ ÓÉÓÔÅÍÙ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ ÔÅËÓÔÁ groff, ÔÒÅÂÕÀÝÁÑ Perl
Summary(uk):	þÁÓÔÉÎÁ ÓÉÓÔÅÍÉ ÆÏÒÍÁÔÕ×ÁÎÎÑ ÔÅËÓÔÕ groff, ÑË¦Ê ÐÏÔÒ¦ÂÅÎ Perl
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description perl
groff-perl contains the parts of the groff text processor package that
require Perl. These include the afmtodit font processor used to create
PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the
troff-to-ps print filter.

%description perl -l pl
groff-perl zawiera czê¶æ zasobów groff-a która wymaga Perla. Skrypt
afmtodit jest procesorem fontów u¿ywanym do tworzenia plików fontów w
formacie PostScript, a skrypt grok u¿ywany jest do automatycznego
doboru parametrów dla groff przy konwersji troff -> PostScript (zwykle
u¿ywany przy drukowaniu).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f config.cache
PATH=$PATH:%{_prefix}/X11R6/bin
%{__autoconf}
CXX="g++"
CC="%{__cc}"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
export CXX CC
%configure
%{__make}


%if %{!?_without_xditview:1}%{?_without_xditview:0}
cd src/xditview
xmkmf
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT
PATH=$PATH:%{_prefix}/X11R6/bin

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/trofftops

%if %{!?_without_xditview:1}%{?_without_xditview:0}
%{__make} -C src/xditview DESTDIR=$RPM_BUILD_ROOT install install.man
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
%{_mandir}/man7/[^m]*

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
%lang(ja) %{_mandir}/ja/man7/[^m]*

%lang(pl) %{_mandir}/pl/man1/gnroff.1*
%lang(pl) %{_mandir}/pl/man1/groff.1*
%lang(pl) %{_mandir}/pl/man1/gsoelim.1*
%lang(pl) %{_mandir}/pl/man1/gtbl.1*
%lang(pl) %{_mandir}/pl/man1/nroff.1*
%lang(pl) %{_mandir}/pl/man1/soelim.1*
%lang(pl) %{_mandir}/pl/man1/tbl.1*

%{_infodir}/*info*

%files gxditview
%if %{!?_without_xditview:1}%{?_without_xditview:0}
%defattr(644,root,root,755)
%doc src/xditview/{ChangeLog,README,TODO}
%attr(755,root,root) %{_xbindir}/gxditview
%{_xlibdir}/X11/app-defaults/GXditview
%{_xmandir}/man1/*
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
