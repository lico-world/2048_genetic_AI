#ifndef INC_2048_GENETIC_AI_ABSTRACTACTIONMANAGER_H
#define INC_2048_GENETIC_AI_ABSTRACTACTIONMANAGER_H

#include <vector>

#include "Action.h"


class AbstractActionManager
{
private:
    std::vector<Action*> _actions;

public:
    AbstractActionManager(unsigned int nbActions);
    std::vector<Action*> getPossibleActions();
    virtual void setActions() = 0;
};


#endif
