#ifndef INC_2048_GENETIC_AI_ABSTRACTDATAHANDLER_H
#define INC_2048_GENETIC_AI_ABSTRACTDATAHANDLER_H

#include <vector>


template <typename T> class AbstractDataHandler
{
private:
    T* _dataInput;
    std::vector<double> _dataOutput;
    unsigned int _dataSize;

public:
    AbstractDataHandler();
    bool setInputData(T* dataInput);
    std::vector<double> requestData(int length);
    virtual bool transformData() = 0;
};


#endif
