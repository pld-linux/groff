Summary:	A document formatting system
Summary(de):	Ein Dokumentformatierungssystem
Summary(fr):	Paquetage de formatage de texte groff de GNU
Summary(pl):	GNU groff - pakiet do formatowania tekstu
Summary(tr):	GNU groff metin bi�emleme paketi
Name:		groff
Version:	1.17
Release:	1
License:	GPL
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Source0:	ftp://ftp.ffii.org/pub/groff/%{name}-%{version}.tar.gz
Source1:	%{name}-trofftops.sh
Patch0:		%{name}-safer.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-info.patch
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
Requires:	mktemp
Obsoletes:	groff-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
erzeugten Dokumente k�nnen angezeigt oder ausgedruckt werden. Groffs
Formatierungsbefehle erlauben Ihnen, Schriftart und -gr��e, Fettdruck,
Kursivdruck, und die Anzahl der Spalten pro Seite usw. zu setzen. Sie
sollten groff installieren, wenn Sie es als
Dokumentformatierungssystem benutzen wollen. Groff ann auch benutzt
werden, um man-pages anzuziegen. Wenn Sie groff in X11 benutzen
wollten, brauchen Sie auch das groff-gxditview-Paket.

%description -l fr
Le syst�me de formatage de texte groff peut �tre utilis� pour cr�er
des documents d'aspect professionnel sur papier et � l'�cran. Toutes
les pages man sont trait�es avec groff, vous avez donc besoin de ce
paquetage pour les visualiser.

%description -l pl
System formatowania tekstu groff mo�e by� u�ywany do tworzenia
profesjonalnie wygl�daj�cego dokumentu zar�wno na papierze jak i na
konsoli. Wszystkie podr�czniki ekranowe (man) potrzebuj� groff'a do
formatowania tekstu na ekranie. Tak wi�c potrzebujesz tego pakietu do
czytania podr�cznik�w ekranowych.

%description -l tr
groff metin bi�emleme sistemi ka��t veya bilgisayar ekran� �zerinde
profesyonel g�r�n�me sahip belgeler yaratmaya yarar. B�t�n k�lavuz
(man) sayfalar� groff ile haz�rlanm��t�r. man sayfalar�n� okuyabilmek
i�in groff paketine gereksiniminiz olacakt�r.

%package gxditview
Summary:	An X previewer for groff text processor output
Summary(de):	X-Anzeiger fuer groff Textprozessor-Ausgaben
Summary(fr):	Le visualiseur de fichier groff de GNU, sous X
Summary(pl):	Groff pod X
Summary(tr):	GNU groff X g�r�nt�leyici
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Requires:	%{name} = %{version}

%description gxditview
Gxditview displays the groff text processor's output on an X Window
System display. If you are going to use groff as a text processor, you
should install gxditview so that you preview your processed text files
in X. You'll also need to install the groff package and the X Window
System.

%description -l de gxditview
Gxditview zeigt groff-Ausgaben auf einem X-Window-Display an. Wenn Sie
groff als Textprozessor benutzen wollen, und X11 benutzen, sollten Sie
gxditview installieren.

%description -l fr gxditview
Ce paquetage contient le programme gxditview, qui peut servir �
formater et viusaliser les documents groff sous X Window. Les pages
peuvent, par exemple, �tre lues avec gxditview.

%description -l pl gxditview
Pakiet ten zawiera program gxditview, kt�ry pozwoli Ci na formatowanie
dokument�w pod X. Na przyk�ad, do czytania por�cznik�w ekranowych.

%description -l tr gxditview
Bu paket groff belgelerini g�r�nt�leyip de�i�tirmeye yarayan gxditview
program�n� i�erir. �rne�in man sayfalar� gxditview kullan�larak
okunabilir.

%package perl
Summary:	Parts of the groff formatting system that require Perl
Summary(pl):	Cze�� zasob�w groff-a kt�ra wymaga Perla
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Requires:	%{name} = %{version}

%description perl
groff-perl contains the parts of the groff text processor package that
require Perl. These include the afmtodit font processor used to create
PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the
troff-to-ps print filter.

%description -l pl perl
groff-perl zawiera cz�� zasob�w groff-a kt�ra wymaga Perla. Skrypt
afmtodit jest procesorem font�w u�ywanym do tworzenia plik�w font�w w
formacie PostScript, a skrypt grok u�ywany jest do automatycznego
doboru parametr�w dla groff przy konwersji troff -> PostScript (zwykle
u�ywany przy drukowaniu).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f config.cache
PATH=$PATH:%{_prefix}/X11R6/bin
autoconf
CXX="g++"
CC="%{__cc}"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
export CXX CC
%configure
%{__make}

cd src/xditview
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
PATH=$PATH:%{_prefix}/X11R6/bin

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/trofftops

%{__make} -C src/xditview DESTDIR=$RPM_BUILD_ROOT install install.man

%{__make} -C doc install DESTDIR=$RPM_BUILD_ROOT infodir="%{_infodir}"

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

gzip -9nf NEWS PROBLEMS PROJECTS README TODO BUG-REPORT ChangeLog \
	src/xditview/{ChangeLog,README,TODO}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,PROBLEMS,PROJECTS,README,TODO,BUG-REPORT,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/addftinfo
%attr(755,root,root) %{_bindir}/eqn
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
%{_mandir}/man1/geqn.1*
%{_mandir}/man1/gindxbib.1*
%{_mandir}/man1/glookbib.1*
%{_mandir}/man1/gneqn.1*
%{_mandir}/man1/gnroff.1*
%{_mandir}/man1/gpic.1*
%{_mandir}/man1/grefer.1*
%{_mandir}/man1/grodvi.1*
%{_mandir}/man1/grn.1*
%{_mandir}/man1/groff.1*
%{_mandir}/man1/grohtml.1*
%{_mandir}/man1/grolj4.1*
%{_mandir}/man1/grolbp.1*
%{_mandir}/man1/grops.1*
%{_mandir}/man1/grotty.1*
%{_mandir}/man1/gsoelim.1*
%{_mandir}/man1/gtbl.1*
%{_mandir}/man1/gtroff.1*
%{_mandir}/man1/hpftodit.1*
%{_mandir}/man1/indxbib.1*
%{_mandir}/man1/lkbib.1*
%{_mandir}/man1/lookbib.1*
%{_mandir}/man1/nroff.1*
%{_mandir}/man1/pfbtops.1*
%{_mandir}/man1/pic.1*
%{_mandir}/man1/refer.1*
%{_mandir}/man1/soelim.1*
%{_mandir}/man1/tbl.1*
%{_mandir}/man1/tfmtodit.1*
%{_mandir}/man1/troff.1*
%{_mandir}/man[57]/*
%{_infodir}/*info*

%files gxditview
%defattr(644,root,root,755)
%doc src/xditview/*.gz
%attr(755,root,root) %{_prefix}/X11R6/bin/gxditview
%{_prefix}/X11R6/lib/X11/app-defaults/GXditview
%{_prefix}/X11R6/man/man1/*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afmtodit
%attr(755,root,root) %{_bindir}/grog
%attr(755,root,root) %{_bindir}/mmroff
%attr(755,root,root) %{_bindir}/trofftops
%{_mandir}/man1/afmtodit.*
%{_mandir}/man1/grog.*
%{_mandir}/man7/mmroff.*
