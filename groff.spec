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
Version:	1.22.4
Release:	2
Epoch:		1
License:	GPL v3+
Group:		Applications/Publishing
Source0:	https://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
# Source0-md5:	08fb04335e2f5e73f23ea4c3adbf0c5f
Source1:	%{name}-trofftops.sh
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	3f8b22cc1eefb53306c8c2acf31aca29
Source3:	%{name}-nroff
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/groff/
BuildRequires:	autoconf >= 2.62
BuildRequires:	libstdc++-devel
BuildRequires:	netpbm-progs
BuildRequires:	perl-base >= 1:5.6.1
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo >= 4.8
BuildRequires:	uchardet-devel >= 0.0.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	mktemp
Requires:	uchardet >= 0.0.1
Obsoletes:	groff-for-man
Obsoletes:	groff-tools
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	perl-base >= 1:5.6.1

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
%patch -P 0 -p1

%build
%{__aclocal} -I m4 -I gnulib_m4
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%configure \
	--docdir=%{_docdir}/%{name}-%{version} \
	--disable-silent-rules \
	--with-appresdir=%{_appdefsdir} \
	--with-grofferdir=%{_datadir}/%{name}/%{version}/groffer \
	--with-urw-fonts=%{_fontsdir}/Type1
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/trofftops
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/nroff

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
echo ".so nroff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gnroff.1
echo ".so pic.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gpic.1
echo ".so refer.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/grefer.1
echo ".so soelim.1" >  $RPM_BUILD_ROOT%{_mandir}/man1/gsoelim.1
echo ".so tbl.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gtbl.1
echo ".so troff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gtroff.1

for f in %{_bindir}/{chem,glilypond,gperl,gpinyin,groffer,roff2dvi,roff2html,roff2pdf,roff2ps,roff2text,roff2x} \
	%{_libdir}/%{name}/{gpinyin,grog}/subs.pl \
	%{_datadir}/%{name}/%{version}/groffer/{main_subs,man,subs}.pl ; do
	grep -q '^#! /usr/bin/env perl' $RPM_BUILD_ROOT$f || exit 1
	sed -i -e '1s,#! /usr/bin/env perl,#!/usr/bin/perl,' $RPM_BUILD_ROOT$f
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/ja/{man7/mmroff.7,man1/mmroff.1}

%{__rm} $RPM_BUILD_ROOT%{_mandir}/ja/man1/geqn.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/ja/man1/gneqn.1

# clean docdir
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc BUG-REPORT ChangeLog LICENSES NEWS PROBLEMS PROJECTS README TODO
%attr(755,root,root) %{_bindir}/addftinfo
%attr(755,root,root) %{_bindir}/eqn
%attr(755,root,root) %{_bindir}/eqn2graph
%attr(755,root,root) %{_bindir}/gdiffmk
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
%attr(755,root,root) %{_bindir}/grolbp
%attr(755,root,root) %{_bindir}/grolj4
%attr(755,root,root) %{_bindir}/gropdf
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
%attr(755,root,root) %{_bindir}/pdfmom
%attr(755,root,root) %{_bindir}/pdfroff
%attr(755,root,root) %{_bindir}/pfbtops
%attr(755,root,root) %{_bindir}/pic
%attr(755,root,root) %{_bindir}/pic2graph
%attr(755,root,root) %{_bindir}/post-grohtml
%attr(755,root,root) %{_bindir}/pre-grohtml
%attr(755,root,root) %{_bindir}/preconv
%attr(755,root,root) %{_bindir}/refer
%attr(755,root,root) %{_bindir}/soelim
%attr(755,root,root) %{_bindir}/tbl
%attr(755,root,root) %{_bindir}/tfmtodit
%attr(755,root,root) %{_bindir}/troff
%dir %{_libdir}/groff
%{_libdir}/groff/groff_opts_*.txt
%dir %{_datadir}/groff
%dir %{_datadir}/groff/%{version}
%{_datadir}/groff/%{version}/eign
%{_datadir}/groff/%{version}/font
%{_datadir}/groff/%{version}/oldfont
%{_datadir}/groff/%{version}/pic
%{_datadir}/groff/%{version}/tmac
%{_datadir}/groff/current
%{_datadir}/groff/site-font
%{_datadir}/groff/site-tmac
%{_mandir}/man1/addftinfo.1*
%{_mandir}/man1/eqn.1*
%{_mandir}/man1/eqn2graph.1*
%{_mandir}/man1/gdiffmk.1*
%{_mandir}/man1/geqn.1*
%{_mandir}/man1/gindxbib.1*
%{_mandir}/man1/glookbib.1*
%{_mandir}/man1/gnroff.1*
%{_mandir}/man1/gpic.1*
%{_mandir}/man1/grap2graph.1*
%{_mandir}/man1/grefer.1*
%{_mandir}/man1/grn.1*
%{_mandir}/man1/grodvi.1*
%{_mandir}/man1/groff.1*
%{_mandir}/man1/grohtml.1*
%{_mandir}/man1/grolbp.1*
%{_mandir}/man1/grolj4.1*
%{_mandir}/man1/gropdf.1*
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
%{_mandir}/man1/pdfmom.1*
%{_mandir}/man1/pdfroff.1*
%{_mandir}/man1/pfbtops.1*
%{_mandir}/man1/pic.1*
%{_mandir}/man1/pic2graph.1*
%{_mandir}/man1/preconv.1*
%{_mandir}/man1/refer.1*
%{_mandir}/man1/soelim.1*
%{_mandir}/man1/tbl.1*
%{_mandir}/man1/tfmtodit.1*
%{_mandir}/man1/troff.1*
%{_mandir}/man5/groff_*.5*
%{_mandir}/man5/lj4_font.5*
%{_mandir}/man7/ditroff.7*
%{_mandir}/man7/groff*.7*
%{_mandir}/man7/roff.7*

%lang(de) %{_mandir}/de/man1/groff.1*

%lang(fi) %{_mandir}/fi/man1/addftinfo.1*

%lang(ja) %{_mandir}/ja/man1/addftinfo.1*
%lang(ja) %{_mandir}/ja/man1/eqn.1*
%lang(ja) %{_mandir}/ja/man1/gindxbib.1*
%lang(ja) %{_mandir}/ja/man1/glookbib.1*
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
%lang(ja) %{_mandir}/ja/man5/groff_*.5*
%lang(ja) %{_mandir}/ja/man7/groff*.7*
%lang(ja) %{_mandir}/ja/man7/roff.7*

%lang(pl) %{_mandir}/pl/man1/gnroff.1*
%lang(pl) %{_mandir}/pl/man1/groff.1*
%lang(pl) %{_mandir}/pl/man1/gsoelim.1*
%lang(pl) %{_mandir}/pl/man1/gtbl.1*
%lang(pl) %{_mandir}/pl/man1/nroff.1*
%lang(pl) %{_mandir}/pl/man1/soelim.1*
%lang(pl) %{_mandir}/pl/man1/tbl.1*

%{_infodir}/groff.info*

%files gxditview
%defattr(644,root,root,755)
%doc src/devices/xditview/{ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/gxditview
%attr(755,root,root) %{_bindir}/xtotroff
%{_appdefsdir}/GXditview
%{_appdefsdir}/GXditview-color
%{_mandir}/man1/gxditview.1*
%{_mandir}/man1/xtotroff.1*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afmtodit
%attr(755,root,root) %{_bindir}/chem
%attr(755,root,root) %{_bindir}/glilypond
%attr(755,root,root) %{_bindir}/gperl
%attr(755,root,root) %{_bindir}/gpinyin
%attr(755,root,root) %{_bindir}/groffer
%attr(755,root,root) %{_bindir}/grog
%attr(755,root,root) %{_bindir}/mmroff
%attr(755,root,root) %{_bindir}/roff2dvi
%attr(755,root,root) %{_bindir}/roff2html
%attr(755,root,root) %{_bindir}/roff2pdf
%attr(755,root,root) %{_bindir}/roff2ps
%attr(755,root,root) %{_bindir}/roff2text
%attr(755,root,root) %{_bindir}/roff2x
%attr(755,root,root) %{_bindir}/trofftops
%{_libdir}/groff/glilypond
%{_libdir}/groff/gpinyin
%{_libdir}/groff/grog
%{_datadir}/groff/%{version}/groffer
%{_mandir}/man1/afmtodit.1*
%{_mandir}/man1/chem.1*
%{_mandir}/man1/glilypond.1*
%{_mandir}/man1/gperl.1*
%{_mandir}/man1/gpinyin.1*
%{_mandir}/man1/grog.1*
%{_mandir}/man1/groffer.1*
%{_mandir}/man1/mmroff.1*
%{_mandir}/man1/roff2dvi.1*
%{_mandir}/man1/roff2html.1*
%{_mandir}/man1/roff2pdf.1*
%{_mandir}/man1/roff2ps.1*
%{_mandir}/man1/roff2text.1*
%{_mandir}/man1/roff2x.1*

%lang(fi) %{_mandir}/fi/man1/afmtodit.1*

%lang(ja) %{_mandir}/ja/man1/grog.1*
%lang(ja) %{_mandir}/ja/man1/mmroff.1*
