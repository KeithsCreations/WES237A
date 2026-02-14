#include "cycletime.h"

void initPMU(void){
    init_counters(1,0);
}

unsigned int getCyclecount(void){
    return get_cyclecount();
}