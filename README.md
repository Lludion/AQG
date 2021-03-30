# AQG ~ Addressable Quantum Gates

 The AQC ( Addressable Quantum Circuit) formalism (or AQG, Addressable Quantum Gates) is a formalism developed by Arrighi,Costes,Cedzich,Rémond & Valiron to encompass coherent quantum control of quantum operations. Indeed, usually, quantum circuits are [\[1\]](https://arxiv.org/abs/2101.08796) applying quantum gates on a quantum system in a purely classical way. It is also possible that this order is changing during the computation, but in a purely classical way. However, quantum gates applied in a quantum superposition of causal orders has also been described [\[2\]](https://arxiv.org/abs/0912.0195). This AQC formalism allows a description of a quantum system whose wiring between gates can be in a superposition of several basis states.

![Example image of an AQC](./data/img/aqcreadme.jpg?raw=true "Title")

### Addressable Quantum Circuits (AQC)

  Details about AQC can be found in [the original paper](https://arxiv.org/abs/2121.01101000011001010110110001110000001000000110110101100101).

 An AQC is a tuple (K,E) where K is a *skeleton* and E is a *configuration* on the skeleton K.

 A **skeleton** K is a tuple (A,G,S,D,*n*) where A is the finite set of addresses, G is the set of gates, S is a function associating to each gate its operator (also called scattering), D is a finite dataset and *n* is an integer.  Upon this skeleton, various states can be formed. They form what will be called here configuration. 
 
 A **configuration** on a skeleton K is a quantum state, which can be a superposition of basis states on K , the defintion of which is quickly sketched below below.

 A **basis state** is a tuple (T,L,D) where:

T is a target, linking each sector to either its *target sector* or the empty word

L is a couple (Li, Lo), linking each sector to its list of input (resp. output) addresses.

D is a couple (Di, Do), linking each sector to its list of input (resp. output) data.

### Remarks

We are not using the extended space (the so-called *named space*) here, as it was proven to be equivalent.

