#ifndef ISNTALLER_H
#define ISNTALLER_H

#include <QMainWindow>

namespace Ui {
class Isntaller;
}

class Isntaller : public QMainWindow
{
    Q_OBJECT

public:
    explicit Isntaller(QWidget *parent = 0);
    ~Isntaller();

private:
    Ui::Isntaller *ui;
};

#endif // ISNTALLER_H
