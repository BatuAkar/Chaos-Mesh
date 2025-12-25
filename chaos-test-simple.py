"""
Simple Chaos Engineering Simulation Test
Tests chaos scenarios without external dependencies
"""
import time
import statistics
from datetime import datetime

class ChaosTest:
    def __init__(self):
        self.results = {}
    
    def test_network_delay_simulation(self):
        """Simulate network delay chaos"""
        print("\n📡 Test 1: Network Delay Chaos (500ms simulated)")
        print("-" * 60)
        
        latencies = []
        delay = 0.5  # 500ms delay
        
        for i in range(10):
            start = time.time()
            # Simulate network delay
            time.sleep(delay)
            latency = (time.time() - start) * 1000
            latencies.append(latency)
            print(f"  Request {i+1}: {latency:.2f}ms")
        
        avg = statistics.mean(latencies)
        print(f"\n✅ Average latency: {avg:.2f}ms (baseline ~{delay*1000:.0f}ms)")
        self.results["Network Delay (500ms)"] = latencies
        return latencies
    
    def test_packet_loss_simulation(self):
        """Simulate packet loss chaos"""
        print("\n📦 Test 2: Packet Loss Chaos (30% loss simulated)")
        print("-" * 60)
        
        import random
        success = 0
        failures = 0
        latencies = []
        packet_loss_rate = 0.30
        
        for i in range(20):
            if random.random() > packet_loss_rate:
                # Simulate successful request
                start = time.time()
                time.sleep(0.05)  # 50ms latency
                latency = (time.time() - start) * 1000
                latencies.append(latency)
                success += 1
                print(f"  Request {i+1}: ✓ Success ({latency:.2f}ms)")
            else:
                failures += 1
                print(f"  Request {i+1}: ✗ Lost (packet loss)")
        
        success_rate = (success / 20) * 100
        print(f"\n📊 Results:")
        print(f"   Successful: {success}/20")
        print(f"   Failed: {failures}/20")
        print(f"   Success Rate: {success_rate:.1f}%")
        
        self.results["Packet Loss (30%)"] = latencies
        return latencies
    
    def test_bandwidth_throttle(self):
        """Simulate bandwidth throttling"""
        print("\n🚦 Test 3: Bandwidth Throttle (1 Mbps simulated)")
        print("-" * 60)
        
        latencies = []
        # Simulate slower throughput (1 Mbps)
        data_size = 1024 * 128  # 128KB
        bandwidth = 1024 * 1024  # 1 Mbps
        expected_time = data_size / bandwidth
        
        for i in range(8):
            start = time.time()
            time.sleep(expected_time)
            latency = (time.time() - start) * 1000
            latencies.append(latency)
            print(f"  Transfer {i+1}: {latency:.2f}ms ({data_size/1024:.0f}KB @ 1Mbps)")
        
        avg = statistics.mean(latencies)
        print(f"\n✅ Average transfer time: {avg:.2f}ms")
        self.results["Bandwidth Throttle (1Mbps)"] = latencies
        return latencies
    
    def test_cpu_stress(self):
        """Simulate CPU stress impact"""
        print("\n⚙️  Test 4: CPU Stress Impact")
        print("-" * 60)
        
        latencies = []
        
        def cpu_intensive():
            result = 0
            for i in range(5000000):
                result += i ** 0.5
            return result
        
        # Normal latency baseline
        print("  Phase 1: Baseline (no stress)")
        baseline = []
        for i in range(3):
            start = time.time()
            time.sleep(0.01)
            latency = (time.time() - start) * 1000
            baseline.append(latency)
            latencies.append(latency)
        
        baseline_avg = statistics.mean(baseline)
        print(f"    Average: {baseline_avg:.2f}ms")
        
        # With CPU stress
        print("  Phase 2: Under CPU stress")
        stressed = []
        for i in range(3):
            start = time.time()
            cpu_intensive()
            latency = (time.time() - start) * 1000
            stressed.append(latency)
            latencies.append(latency)
        
        stressed_avg = statistics.mean(stressed)
        print(f"    Average: {stressed_avg:.2f}ms")
        
        increase = ((stressed_avg - baseline_avg) / baseline_avg) * 100
        print(f"\n✅ Performance degradation: {increase:.1f}%")
        
        self.results["CPU Stress"] = latencies
        return latencies
    
    def test_cascading_failure(self):
        """Simulate cascading failure"""
        print("\n🔗 Test 5: Cascading Failure")
        print("-" * 60)
        
        latencies = []
        
        print("  Phase 1: Normal operation")
        success = 0
        for i in range(3):
            start = time.time()
            time.sleep(0.05)
            latency = (time.time() - start) * 1000
            latencies.append(latency)
            success += 1
            print(f"    Request {i+1}: ✓ Success ({latency:.2f}ms)")
        
        print("  Phase 2: Service degradation (backend slow)")
        for i in range(3):
            start = time.time()
            time.sleep(0.3)  # Simulate slow backend
            latency = (time.time() - start) * 1000
            latencies.append(latency)
            print(f"    Request {i+1}: ⚠️  Slow ({latency:.2f}ms)")
        
        print("  Phase 3: Service failure (backend down)")
        failures = 0
        for i in range(3):
            failures += 1
            print(f"    Request {i+1}: ✗ Failed (backend unavailable)")
        
        total = success + 6
        failure_rate = (failures / total) * 100
        print(f"\n📊 Results:")
        print(f"   Initial success: {success}/3")
        print(f"   Degraded requests: 3/3")
        print(f"   Failed requests: {failures}/3")
        print(f"   Overall failure rate: {failure_rate:.1f}%")
        
        self.results["Cascading Failure"] = latencies
        return latencies
    
    def test_dns_chaos(self):
        """Simulate DNS chaos"""
        print("\n📛 Test 6: DNS Chaos (name resolution delays)")
        print("-" * 60)
        
        latencies = []
        dns_delay = 0.2  # 200ms DNS delay
        
        print("  DNS Resolution attempts:")
        for i in range(8):
            start = time.time()
            time.sleep(dns_delay)  # Simulate DNS lookup delay
            latency = (time.time() - start) * 1000
            latencies.append(latency)
            print(f"  Lookup {i+1}: {latency:.2f}ms (backend service)")
        
        avg = statistics.mean(latencies)
        print(f"\n✅ Average DNS resolution time: {avg:.2f}ms")
        self.results["DNS Chaos"] = latencies
        return latencies
    
    def test_memory_pressure(self):
        """Simulate memory pressure"""
        print("\n💾 Test 7: Memory Pressure")
        print("-" * 60)
        
        latencies = []
        
        print("  Allocating memory and measuring request latency:")
        # Simulate memory allocation
        memory_chunk = []
        
        for i in range(5):
            try:
                # Allocate some memory
                memory_chunk.append([0] * 10000000)  # ~40MB each
                
                start = time.time()
                time.sleep(0.1)  # Simulate request processing
                latency = (time.time() - start) * 1000
                latencies.append(latency)
                
                memory_used = len(memory_chunk) * 40
                print(f"  Request {i+1} (Memory: ~{memory_used}MB): {latency:.2f}ms")
                
            except MemoryError:
                print(f"  Request {i+1}: Memory limit reached")
                break
        
        if latencies:
            avg = statistics.mean(latencies)
            print(f"\n✅ Average latency under memory pressure: {avg:.2f}ms")
        
        self.results["Memory Pressure"] = latencies
        return latencies
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n" + "="*80)
        print("CHAOS ENGINEERING TEST REPORT")
        print("="*80)
        print(f"Generated: {datetime.now().isoformat()}")
        print("="*80)
        
        total_latencies = []
        
        for test_name, latencies in self.results.items():
            if latencies:
                avg = statistics.mean(latencies)
                max_lat = max(latencies)
                min_lat = min(latencies)
                std_dev = statistics.stdev(latencies) if len(latencies) > 1 else 0
                
                total_latencies.extend(latencies)
                
                print(f"\n📊 {test_name}")
                print(f"   Average: {avg:.2f}ms")
                print(f"   Maximum: {max_lat:.2f}ms")
                print(f"   Minimum: {min_lat:.2f}ms")
                print(f"   Std Dev: {std_dev:.2f}ms")
                print(f"   Samples: {len(latencies)}")
        
        if total_latencies:
            print("\n" + "="*80)
            print("📈 OVERALL STATISTICS")
            print("="*80)
            sorted_lat = sorted(total_latencies)
            print(f"Total Requests: {len(total_latencies)}")
            print(f"Average Latency: {statistics.mean(total_latencies):.2f}ms")
            print(f"Median Latency: {statistics.median(total_latencies):.2f}ms")
            print(f"P99 Latency: {sorted_lat[int(len(sorted_lat)*0.99)-1]:.2f}ms")
            print(f"P95 Latency: {sorted_lat[int(len(sorted_lat)*0.95)-1]:.2f}ms")
            print(f"Max Latency: {max(total_latencies):.2f}ms")
        
        print("\n" + "="*80)
        print("✅ TEST SUITE COMPLETED")
        print("="*80)

def main():
    print("\n" + "="*80)
    print("CHAOS ENGINEERING - SIMULATION TEST SUITE")
    print("="*80)
    print("Testing various chaos scenarios with simulated conditions")
    print("="*80)
    
    tester = ChaosTest()
    
    try:
        # Run all tests
        tester.test_network_delay_simulation()
        tester.test_packet_loss_simulation()
        tester.test_bandwidth_throttle()
        tester.test_cpu_stress()
        tester.test_cascading_failure()
        tester.test_dns_chaos()
        tester.test_memory_pressure()
        
        # Generate report
        tester.generate_report()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
