#ifndef INC_2048_GENETIC_AI_DATAHANDLER2048_H
#define INC_2048_GENETIC_AI_DATAHANDLER2048_H

#include "../../general_agent/include/AbstractDataHandler.h"

class DataHandler2048 : public AbstractDataHandler<unsigned short>
{
private:


public:
    DataHandler2048();
    bool transformData() override;
};


#endif
