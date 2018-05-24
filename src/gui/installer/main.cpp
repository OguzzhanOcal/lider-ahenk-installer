#include "isntaller.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Isntaller w;
    w.show();

    return a.exec();
}
