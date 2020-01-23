# Test the speed of your PyOpenCL program
from time import time  # Import time tools

import pyopencl as cl  # Import the OpenCL GPU computing API
import numpy as np  # Import number tools
import PyOpeClDeviceInfo as device_info

a = np.random.rand(10000).astype(np.float32)  # Create a random array to add
b = np.random.rand(10000).astype(np.float32)  # Create a random array to add

def cpu_array_sum(a, b):  # Sum two arrays on the CPU
    c_cpu = np.empty_like(a)  # Create the destination array
    cpu_start_time = time()  # Get the CPU start time
    for i in range(10000):
            for j in range(10000):  # 1000 times add each number and store it
                    c_cpu[i] = a[i] + b[i]  # This add operation happens 1,000,000 times XXX
    cpu_end_time = time()  # Get the CPU end time
    print("CPU Time: {0} s".format(cpu_end_time - cpu_start_time))  # Print how long the CPU took
    return c_cpu  # Return the sum of the arrays

def gpu_array_sum(a, b):
    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]
    context = cl.Context([device])
    queue = cl.CommandQueue(context, properties=cl.command_queue_properties.PROFILING_ENABLE)  # Instantiate a Queue with profiling (timing) enabled
    a_buffer = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=a)
    b_buffer = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b)
    c_buffer = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, b.nbytes)  # Create three buffers (plans for areas of memory on the device)
    program = cl.Program(context, """
    __kernel void sum(__global const float *a, __global const float *b, __global float *c)
    {
        int i = get_global_id(0);
        int j;
        for(j = 0; j < 10000; j++)
        {
            c[i] = a[i] + b[i];
        }
    }""").build()  # Compile the device program
    gpu_start_time = time()  # Get the GPU start time
    event = program.sum(queue, a.shape, None, a_buffer, b_buffer, c_buffer)  # Enqueue the GPU sum program XXX
    event.wait()  # Wait until the event finishes XXX
    elapsed = 1e-9*(event.profile.end - event.profile.start)  # Calculate the time it took to execute the kernel
    print("GPU Kernel Time: {0} s".format(elapsed))  # Print the time it took to execute the kernel
    c_gpu = np.empty_like(a)  # Create an empty array the same size as array a
    cl.enqueue_read_buffer(queue, c_buffer, c_gpu).wait()  # Read back the data from GPU memory into array c_gpu
    gpu_end_time = time()  # Get the GPU end time
    print("GPU Time: {0} s".format(gpu_end_time - gpu_start_time))  # Print the time the GPU program took, including both memory copies
    return c_gpu  # Return the sum of the two arrays



if __name__ == "__main__":
    device_info.print_device_info()
    cpu_array_sum(a, b)  # Call the function that sums two arrays on the CPU
    gpu_array_sum(a, b)  # Call the function that sums two arrays on the GPU
    assert (la.norm(cpu_result - gpu_result)) < 1e-5
