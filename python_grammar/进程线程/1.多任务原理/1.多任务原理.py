"""



现代操作系统（Windows Mac OS X Linux UNIX）都支持多任务

就是操作系统同时可以运行多个任务

单核CPU实现多任务原理
让操作系统轮流让各个任务交替执行，例如QQ执行2ms切换到下一个程序然后执行2ms继续切换
表面上看，每个任务反复执行，但是CPU调度执行的速度太快了，导致我们感觉就像所有任务都同时执行一样


多核CPU实现多任务原理
真正的并行执行多任务只能在多核CPU上实现，但是由于任务的数量远远多于CPU
的核心数量，所以操作系统也会自动把很多任务轮流调度到每个核心上执行
并发：看上去一起执行，任务数多于CPU核心数
并行：真正一起执行，任务数小于CPU核心数


实现多任务的方式：
1.多进程模式
2.多线程模式
3.协程模式
4.多线程+多进程模式










"""