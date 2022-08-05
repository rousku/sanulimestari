# sanulimestari

Profiling (from C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof):                                               
Fri Aug  5 12:31:58 2022    C:\Users\joonas.harjumaki\git\sanulimestari\prof\combined.prof                                     
                                                                                                                               
         335331 function calls (334452 primitive calls) in 1950.944 seconds                                                    
                                                                                                                               
   Ordered by: cumulative time                                                                                                 
   List reduced from 749 to 20 due to restriction <20>                                                                         
                                                                                                                               
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                                        
       16    0.000    0.000 1950.944  121.934 runner.py:108(pytest_runtest_protocol)                                           
       16    0.000    0.000 1950.938  121.934 runner.py:116(runtestprotocol)                                                   
       48    0.000    0.000 1950.937   40.645 runner.py:216(call_and_report)                                                   
  318/176    0.001    0.000 1950.937   11.085 _hooks.py:244(__call__)                                                          
  318/176    0.000    0.000 1950.937   11.085 _manager.py:77(_hookexec)                                                        
  318/176    0.002    0.000 1950.936   11.085 _callers.py:9(_multicall)                                                        
       48    0.000    0.000 1950.927   40.644 runner.py:244(call_runtest_hook)                                                 
       48    0.000    0.000 1950.926   40.644 runner.py:315(from_call)                                                         
       48    0.000    0.000 1950.926   40.644 runner.py:259(<lambda>)                                                          
       16    0.000    0.000 1950.906  121.932 runner.py:157(pytest_runtest_call)                                               
       16    0.000    0.000 1950.905  121.932 python.py:1759(runtest)                                                          
       16    0.000    0.000 1950.905  121.932 python.py:185(pytest_pyfunc_call)                                                
        1    0.000    0.000 1950.904 1950.904 test_sanulimestari.py:49(test_get_best_guess)                                    
        1    0.011    0.011 1950.903 1950.903 __init__.py:121(get_best_guess)                                                  
        4    0.000    0.000 1950.522  487.631 threading.py:534(wait)                                                           
        4    0.000    0.000 1950.522  487.631 threading.py:264(wait)                                                           
       19 1950.522  102.659 1950.522  102.659 {method 'acquire' of '_thread.lock' objects}                                     
        1    0.000    0.000 1950.520 1950.520 pool.py:263(map)                                                                 
        1    0.000    0.000 1950.520 1950.520 pool.py:650(get)                                                                 
        1    0.000    0.000 1950.520 1950.520 pool.py:647(wait)      