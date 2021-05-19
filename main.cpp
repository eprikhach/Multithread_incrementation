#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
#include </Users/eugene_prikhach/Downloads/Python-3.7.10/Include/Python.h>


int increment(int thread_num, int incr_number) {
    std::atomic<unsigned long long> g_count{0};

    std::vector<std::thread> th_vec;
    for (int i = 0; i < thread_num; ++i) {
        th_vec.push_back(std::thread([&]() {
            for (auto i = 0; i < incr_number; ++i)
                g_count.fetch_add(1);
        }));
    }
        for (int i = 0; i < thread_num; ++i) {
            th_vec.at(i).join();
        }

        return g_count;

}


static PyObject* incrementation(PyObject* self, PyObject* args){
    int a;
    int b;
    if (!PyArg_ParseTuple(args,"ii",&a,&b))
        return NULL;
    int result = increment(a,b);
    return Py_BuildValue("i",result);
}

static PyMethodDef mainMethods[] = {
        {"incrementation", incrementation,METH_VARARGS,"increment 0 n times"},
        {NULL,NULL,0,NULL}
};

static PyModuleDef incr = {
        PyModuleDef_HEAD_INIT,
        "incr","Increment Calculation",
        -1,
        mainMethods
};

PyMODINIT_FUNC PyInit_incr(void){
    return PyModule_Create(&incr);
}
