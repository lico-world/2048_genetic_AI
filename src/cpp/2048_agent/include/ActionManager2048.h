#ifndef INC_2048_GENETIC_AI_ACTIONMANAGER2048_H
#define INC_2048_GENETIC_AI_ACTIONMANAGER2048_H

#include "../../general_agent/include/AbstractActionManager.h"

class ActionManager2048 : public AbstractActionManager
{
private:


public:
    ActionManager2048(unsigned int nbActions);
    void setActions() override;
};


#endif
