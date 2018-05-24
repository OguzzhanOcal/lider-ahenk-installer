#include "isntaller.h"
#include "ui_isntaller.h"

Isntaller::Isntaller(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Isntaller)
{
    ui->setupUi(this);
}

Isntaller::~Isntaller()
{
    delete ui;
}
