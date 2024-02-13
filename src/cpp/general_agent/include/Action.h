#ifndef INC_2048_GENETIC_AI_ACTION_H
#define INC_2048_GENETIC_AI_ACTION_H


class Action
{
private:
    unsigned int _id;

public:
    Action(unsigned int id);
    uint32_t getId();
};


#endif
